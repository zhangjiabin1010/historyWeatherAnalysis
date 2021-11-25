import datetime
import time
import traceback

import pandas as pd
import logging

import requests
from bs4 import BeautifulSoup

from weatherCrawler.db import db

logger = logging.getLogger('log')


# 获取指定时间范围内的日期列表
def getDate(startDate,endDate,dateType):
    '''
    参数说明:
    startData: 开始日期
    endData: 结束日期
    dataType: 要获取日期的类型(年、月、日)
    '''
    try:
        if dateType == 'year':
            year = pd.date_range(startDate, endDate, freq='Y')
            dateList = year[1:].year.tolist()
        elif dateType == 'month':
            month = pd.date_range(startDate, endDate, freq='m')
            dateList = month.strftime('%Y%m').tolist()
        else:
            day = pd.date_range(startDate, endDate, freq='D')
            dateList = day.strftime('%Y%m%d').tolist()
        logger.info(f'获取日期列表成功')
        return dateList
    except Exception:
        logger.error(f'获取日期列表异常：{traceback.format_exc()}')
        return False

dateList = getDate('20210801', '20210901', 'month')
# 构建待抓取页面的Url链接
def constructUrl(dateList,city,urlType):
    '''
    参数说明:
    dateList: 指定范围内的日期列表
    city: 指定要爬取的城市
    urlType: 要构建天气或者空气质量的url
    '''
    try:
        urlList = []
        for date in dateList:
            # 获取历史天气信息的url构造规则
            if urlType == 'weather':
                url = f'http://www.tianqihoubao.com/lishi/{city}/month/{date}.html'
            # 获取历史空气质量信息的url构造规则
            else:
                url = f'http://www.tianqihoubao.com/aqi/{city}-{date}.html'
            urlList.append(url)
        logger.info(f'构造{urlType}url列表成功')
        return urlList
    except Exception:
        logger.error(f'构造{urlType}url列表异常：{traceback.format_exc()}')
        return False

# 请求并解析指定url的网页
def getHtmlData(url):
    '''
    参数说明:
    url: 要解析页面的url连接
    '''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        html = requests.get(url,headers=headers)
        #encoding是从http中的header中的charset字段中提取的编码方式，若header中没有charset字段则默认为ISO-8859-1编码模式，则无法解析中文，这是乱码的原因
        # apparent_encoding会从网页的内容中分析网页编码的方式，所以apparent_encoding比encoding更加准确。当网页出现乱码时可以把apparent_encoding的编码格式赋值给encoding。
        html.encoding = html.apparent_encoding
        #使用BeautifulSoup lxml解析库对网页进行解析
        htmlInfo = BeautifulSoup(html.text, 'lxml')
        return htmlInfo
    except Exception:
        logger.error(f'解析url{url}异常：{traceback.format_exc()}')
        return False

# 获取并解析天气数据页面,获取天气数据
def getWeatherData(city):
    '''
    参数说明:
    dateList: 指定要抓取天气数据的时间范围
    city: 指定要抓取天气数据的城市
    '''
    try:
        # 指定构造url的类型为历史天气url
        urlType = 'weather'
        # 构建一定时间范围内的url列表
        urlList = constructUrl(dateList, city, urlType)
        # 循环每个url
        for url in urlList:
            print('天气URL',url)
            time.sleep(2)

            # 获取每个url的网页数据
            htmlInfo = getHtmlData(url)
            # 先获取城市信息，通过id为content class为wdstail定位到标题
            cityinfo = htmlInfo.find('div', attrs={'id': 'content','class':'wdetail'})
            # 获取城市名
            city = cityinfo.find('h1').get_text().strip().split('历史')[0]
            # 通过定位class为b的表格找到数据列表
            tableInfo = htmlInfo.find('table', attrs={'class': 'b'})
            # 寻找表格内的tr标签,获取所有行数据
            trinfo = tableInfo.find_all('tr')
            sqllist = []
            for tr in trinfo[1:]:
                # 循环行数据的每一列，获取天气、温度、风力等信息，并处理数据格式。
                td = tr.find_all('td')
                # weather_date = td[0].find('a')['title'].replace('北京天气预报','').replace('年','-').replace('月','-').replace('日','')
                urlDate = td[0].find('a').get('href').split('.')[0].split('/')[-1]
                weather_date = datetime.datetime.strftime(datetime.datetime.strptime(urlDate, "%Y%m%d"), "%Y-%m-%d")
                weather = td[1].get_text().replace('\r\n', '').replace(' ', '')  #获取天气状况
                temperature = td[2].get_text().strip().replace(' ', '').replace('\r\n', '')  # 获取温度
                wind = td[3].get_text().strip().replace(' ', '').replace('\r\n', '')  # 获取风力大小
                # 拼接插入sql
                sql = f"""insert into weather_original_tab(city,weather,temperature,wind,weather_date) values('{city}','{weather}','{temperature}','{wind}','{weather_date}')"""
                sqllist.append(sql)
            # 调用数据库连接池 执行插入语句，进行数据入库
            insertResult = db.sqlinserts(sqllist)
            if insertResult:
                logger.error(f'抓取天气数据异常 城市:{city} URL:{url} ：{traceback.format_exc()}')
        logger.info(f'抓取天气数据成功 城市:{city}')

    except Exception:
        logger.error(f'抓取天气数据异常 城市:{city} ,原因：{traceback.format_exc()}')
        return False

# 获取并解析空气质量数据页面,获取空气质量数据
def getAqiData(city):
    '''
    参数说明:
    dateList: 指定要抓取空气质量数据的时间范围
    city: 指定要抓取空气质量数据的城市
    '''
    try:
        # 指定构造url的类型为历史空气质量url
        urlType = 'aqi'
        # 构建一定时间范围内的url列表
        urlList = constructUrl(dateList, city, urlType)
        for url in urlList:
            print('空气质量url',url)
            time.sleep(2)
            htmlInfo = getHtmlData(url)
            cityinfo = htmlInfo.find('div', attrs={'id': 'content','class':'wdetail'})


            city = cityinfo.find('h1').get_text().strip().split('空气质量指数')[0][-2:]
            tableInfo = htmlInfo.find('table', attrs={'class': 'b'})
            trinfo = tableInfo.find_all('tr')
            sqllist = []
            for tr in trinfo[1:]:
                # 循环行数据的每一列，获取空气状况，空气指数，pm25指数等其他空气质量数据并处理数据格式。
                td = tr.find_all('td')
                weather_date = td[0].get_text().strip()
                aqi_status = td[1].get_text().strip()
                aqi_index = td[2].get_text().strip()
                aqi_rank = td[3].get_text().strip()
                pm25 = td[4].get_text().strip()
                pm10 = td[5].get_text().strip()
                so2 = td[6].get_text().strip()
                no2 = td[7].get_text().strip()
                co = td[8].get_text().strip()
                o3 = td[9].get_text().strip()
                updatesql = f"""update weather_original_tab set aqi_status = '{aqi_status}',aqi_index = '{aqi_index}',aqi_rank = '{aqi_rank}',pm25 = '{pm25}',pm10 = '{pm10}',so2 = '{so2}',no2 = '{no2}',co = '{co}',o3 = '{o3}' where weather_date = '{weather_date}' and city = '{city}'"""
                # print(weather_date,aqi_status,aqi_index,aqi_rank,pm25,pm10,so2,no2,co,o3)
                sqllist.append(updatesql)
            updateReuslt = db.sqlinserts(sqllist)
            if updateReuslt:
                logger.error(f'抓取空气质量数据异常 城市:{city} URL:{url} ：{traceback.format_exc()}')
        logger.info(f'抓取空气质量数据成功 城市:{city}')
    except Exception:
        logger.error(f'抓取空气质量数据异常 {city}城市 ,原因：{traceback.format_exc()}')
        return False

# 抓取国内主要城市列表
def getCityList():
    try:
        # 抓取国内主要城市列表
        url = 'http://www.tianqihoubao.com/lishi/'
        # 通过BeautifulSoup来获取指定url的html页面
        cityHtml = getHtmlData(url)
        # 寻找class为box pcity的div标签
        cityinfo = cityHtml.find('div', attrs={'class': 'box pcity'})
        # 可以观察到城市被包含在a标签中，所以先定位到a标签
        cityUrl = cityinfo.find_all('a')
        cityList = []
        # 对定位的a标签进行数据处理并进行抓取，添加到列表中
        for a in cityUrl:
            city=a.get('href').split('.')[0].split('/')[-1]
            cityList.append(city)
        return cityList
    except Exception:
        logger.error(f'抓取国内主要城市列表异常：{traceback.format_exc()}')
        return False


if __name__ == '__main__':
    # from multiprocessing.pool import ThreadPool
    cityList = getCityList()
    print(cityList)

    # cityList = ['shanghai', 'tianjin', 'chongqing', 'haerbin', 'changchun', 'shenyang', 'huhehaote', 'shijiazhuang', 'taiyuan', 'xian', 'jinan', 'wulumuqi', 'lasa', 'xining', 'lanzhou', 'yinchuan', 'nanjing', 'wuhan', 'hangzhou', 'hefei', 'fujianfuzhou', 'nanchang', 'changsha', 'guiyang', 'chengdu', 'guangzhou', 'kunming', 'nanning', 'haikou', 'taibei']
    # dateList = getDate('20191001', '20210805', 'month')
    # 北京上海天津重庆哈尔滨长春沈阳呼和浩特石家庄太原西安济南乌鲁木齐拉萨西宁 兰州银川郑州南京武汉杭州合肥福州南昌长沙贵阳成都广州昆明南宁深圳
    # pool = ThreadPool(processes=20)
    # pool.map(getAqiData, (city for city in cityList))
    # # pool.map(getWeatherData, (city for city in cityList))
    # pool.close()
    # pool.join()
    # for city in cityList:
        # getWeatherData(city)
        # getAqiData(city)
    # # city = 'beijing'
    # # getWeatherData(dateList,city)
    # getAqiData(dateList,city)

