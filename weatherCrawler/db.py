import importlib
import time

from DBUtils.PooledDB import PooledDB


class PTConnectionPool(object):
    # 数据库连接信息 子类继承时需修改
    config = None
    # 数据库连接编码
    DB_CHARSET = "utf8"

    # mincached : 启动时开启的闲置连接数量(缺省值 0 以为着开始时不创建连接)
    DB_MIN_CACHED = 10

    # maxcached : 连接池中允许的闲置的最多连接数量(缺省值 0 代表不闲置连接池大小)
    DB_MAX_CACHED = 10

    # maxshared : 共享连接数允许的最大数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量,被请求为共享的连接将会被共享使用
    DB_MAX_SHARED = 20

    # maxconnecyions : 创建连接池的最大数量(缺省值 0 代表不限制)
    DB_MAX_CONNECYIONS = 200

    # blocking : 设置在连接池达到最大数量时的行为(缺省值 0 或 False 代表返回一个错误<toMany......> 其他代表阻塞直到连接数减少,连接被分配)
    DB_BLOCKING = True

    # maxusage : 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用).当达到最大数时,连接会自动重新连接(关闭和重新打开)
    DB_MAX_USAGE = 0

    # setsession : 一个可选的SQL命令列表用于准备每个会话，如["set datestyle to german", ...]
    DB_SET_SESSION = None

    __pool = None

    conn = None
    # 数据库类型
    DB_TYPE = None

    read_timeout = None

    write_timeout = None
    def __enter__(self):
        return self

    def get_pool(self):
        if self.config is None:
            raise KeyError("config is None")
        if self.__pool is None:
            db_creator = importlib.import_module(self.DB_TYPE)
            self.__pool = PooledDB(creator=db_creator, mincached=self.DB_MIN_CACHED, maxcached=self.DB_MAX_CACHED,
                                   maxshared=self.DB_MAX_SHARED, maxconnections=self.DB_MAX_CONNECYIONS,
                                   blocking=self.DB_BLOCKING, maxusage=self.DB_MAX_USAGE,
                                   setsession=self.DB_SET_SESSION, **self.config)

    def sqlselect(self, sql, dict_mark=False, run_time=False, key_lower=False, transform=False):
        """
        执行查询语句，获取结果
        :param sql:sql语句，注意防注入
        :param dict_mark:是否以字典形式返回，默认为False
        :param run_time:是否返回执行时间，默认为False
        :param key_lower:是否将所查询的字典类型的结果的key转化为小写，默认为False
        :param transform:是否将返回结果为None类型的值改为'', 默认为False
        :return:结果集
        """
        time_start = time.time()
        conn = self.__pool.connection()
        cursor = conn.cursor()
        try:
            result = []
            if dict_mark:
                cursor.execute(sql)
                # name为description的第一个内容，表示为字段名
                if key_lower:
                    fields = [desc[0].lower() for desc in cursor.description]
                else:
                    fields = [desc[0] for desc in cursor.description]
                rst = cursor.fetchall()
                if rst:
                    if transform:
                        result = [dict(zip(fields, tuple('' if row is None else row for row in rows))) for rows in rst]
                    else:
                        result = [dict(zip(fields, rows)) for rows in rst]
            else:
                cursor.execute(sql)
                result = cursor.fetchall()
                if transform:
                    result = [tuple('' if row is None else row for row in rows) for rows in result]
        except Exception as e:
            result = str(e)
        finally:
            cursor.close()
            conn.close()
        time_end = time.time()
        if run_time:
            return result, time_end - time_start
        return result

    def sqlinsert(self, sql, run_time=False, *args, **kwargs):
        """
        数据库单条插入
        :param sql:sql语句，注意防注入
        :param run_time:是否返回执行时间，默认为False
        :return:如果 run_time 为真 返回执行时间（dict） 执行正常就是空（None）    异常就是异常信心（str）
        """
        time_start = time.time()
        conn = self.__pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            return str(e)
        finally:
            cursor.close()
            conn.close()
        time_end = time.time()
        if run_time:
            return {"run_time": time_end - time_start}

    def sqlinserts(self, sqllist, run_time=False, *args, **kwargs):
        """
        数据库多条插入
        :param sqllist:sql语句列表，注意防注入
        :param run_time:是否返回执行时间，默认为False
        :return:如果 run_time 为真 返回执行时间（dict） 执行正常就是空（None）    异常就是异常信心（str）
        """
        time_start = time.time()
        conn = self.__pool.connection()
        cursor = conn.cursor()
        try:
            for sql in sqllist:
                try:
                    cursor.execute(sql)
                except Exception as error:
                    return sql + str(error)
            conn.commit()
        except Exception as error:
            return "commit error" + str(error)
        finally:
            cursor.close()
            conn.close()
        time_end = time.time()
        if run_time:
            return {"run_time": time_end - time_start}

    def sqlinserts_sql_params(self, sql_params, run_time=False, *args, **kwargs):
        """
        数据库预编译多条插入
        :param sql_params:sql语句，参数列表，注意防注入
        :param run_time:是否返回执行时间，默认为False
        :return:如果 run_time 为真 返回执行时间（dict） 执行正常就是空（None）    异常就是异常信心（str）
        """
        time_start = time.time()
        conn = self.__pool.connection()
        cursor = conn.cursor()
        try:
            for sql_param in sql_params:
                sql, param = sql_param
                try:
                    cursor.execute(sql, param)
                except Exception as error:
                    return sql + str(error)
                conn.commit()
        except Exception as error:
            return "commit error" + str(error)
        finally:
            cursor.close()
            conn.close()
        time_end = time.time()
        if run_time:
            return {"run_time": time_end - time_start}

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_info(self):
        info = {
            'init_conn_number': self.DB_MIN_CACHED,
            'can_use_conn_number': len(self.__pool._idle_cache),
            'used_conn_number': self.__pool._connections

        }
        return info


class connectMysql(PTConnectionPool):
    DB_TYPE = "pymysql"

    def __init__(self, username=None, passwd=None, ip=None, sid=None, port='3306', sql_config=None, database_id=None,
                 **kwargs):
        if sql_config:
            if len(sql_config[database_id]) == 5:
                username, passwd, ip, port, sid = sql_config[database_id]
            else:
                username, passwd, ip, sid = sql_config[database_id]
        self.config = {
            'host': ip,
            'port': port,
            'database': sid,
            'user': username,
            'password': passwd,
            'charset': self.DB_CHARSET
        }
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
        self.get_pool()


db = connectMysql(username='root', passwd='beiwei1010', ip='59.110.115.32', port=3306,sid='weatherAnalysis', DB_MIN_CACHED=5)
