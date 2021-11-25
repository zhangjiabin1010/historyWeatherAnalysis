from collections import Counter
from pandas import Grouper
import pandas as pd
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pandas.core.frame import DataFrame
from pyecharts import options as opts
from pyecharts.charts import Pie
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./weatherCrawler/templates"))
from pyecharts import options as opts
from pyecharts.charts import Bar,Pie,Line,Page,Tab
from weatherCrawler.db import db
from pandas.core.frame import DataFrame

def getData(date_type):
    if date_type == 'days':
        sql = """select * from weather_original_tab where city = '北京' and weather_date > '2021-07-21' and weather_date < '2021-08-01'"""
    else:
        sql = """select * from weather_original_tab where city = '北京' and weather_date < '2021-08-01' order by weather_date"""

    result = db.sqlselect(sql,dict_mark=True)
    return result

# if __name__ == '__main__':
#     data = getData()
#     data = DataFrame(data)


# data = [{'id': 64, 'city': '北京', 'weather_date': '2021-04-01', 'weather': '多云/阴', 'temperature': '18℃/11℃', 'wind': '东风1-2级/东风1-2级', 'aqi_status': '轻度污染', 'aqi_index': '113', 'aqi_rank': '351', 'pm25': '73', 'pm10': '176', 'so2': '8', 'no2': '44', 'co': '0.93', 'o3': '78'}, {'id': 65, 'city': '北京', 'weather_date': '2021-04-02', 'weather': '阴/小雨', 'temperature': '18℃/10℃', 'wind': '北风1-2级/北风1-2级', 'aqi_status': '良', 'aqi_index': '59', 'aqi_rank': '281', 'pm25': '36', 'pm10': '68', 'so2': '2', 'no2': '26', 'co': '0.45', 'o3': '73'}, {'id': 66, 'city': '北京', 'weather_date': '2021-04-03', 'weather': '多云/晴', 'temperature': '18℃/6℃', 'wind': '北风1-2级/北风1-2级', 'aqi_status': '优', 'aqi_index': '37', 'aqi_rank': '173', 'pm25': '13', 'pm10': '27', 'so2': '2', 'no2': '18', 'co': '0.27', 'o3': '65'}, {'id': 67, 'city': '北京', 'weather_date': '2021-04-04', 'weather': '晴/多云', 'temperature': '20℃/7℃', 'wind': '西南风1-2级/西南风1-2级', 'aqi_status': '优', 'aqi_index': '32', 'aqi_rank': '77', 'pm25': '6', 'pm10': '28', 'so2': '2', 'no2': '20', 'co': '0.22', 'o3': '68'}, {'id': 68, 'city': '北京', 'weather_date': '2021-04-05', 'weather': '多云/多云', 'temperature': '18℃/9℃', 'wind': '西南风1-2级/西南风1-2级', 'aqi_status': '良', 'aqi_index': '60', 'aqi_rank': '279', 'pm25': '30', 'pm10': '70', 'so2': '3', 'no2': '29', 'co': '0.38', 'o3': '68'}, {'id': 69, 'city': '北京', 'weather_date': '2021-04-06', 'weather': '多云/多云', 'temperature': '21℃/10℃', 'wind': '西南风1-2级/西南风1-2级', 'aqi_status': '良', 'aqi_index': '55', 'aqi_rank': '190', 'pm25': '30', 'pm10': '60', 'so2': '2', 'no2': '31', 'co': '0.39', 'o3': '73'}, {'id': 70, 'city': '北京', 'weather_date': '2021-04-07', 'weather': '晴/晴', 'temperature': '20℃/5℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '66', 'aqi_rank': '283', 'pm25': '39', 'pm10': '81', 'so2': '4', 'no2': '35', 'co': '0.51', 'o3': '67'}, {'id': 71, 'city': '北京', 'weather_date': '2021-04-08', 'weather': '晴/多云', 'temperature': '20℃/8℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '64', 'aqi_rank': '280', 'pm25': '33', 'pm10': '72', 'so2': '3', 'no2': '34', 'co': '0.42', 'o3': '69'}, {'id': 72, 'city': '北京', 'weather_date': '2021-04-09', 'weather': '多云/多云', 'temperature': '18℃/6℃', 'wind': '东风1-2级/东风1-2级', 'aqi_status': '良', 'aqi_index': '64', 'aqi_rank': '265', 'pm25': '40', 'pm10': '77', 'so2': '6', 'no2': '33', 'co': '0.65', 'o3': '74'}, {'id': 73, 'city': '北京', 'weather_date': '2021-04-10', 'weather': '多云/多云', 'temperature': '19℃/12℃', 'wind': '西南风3-4级/西南风3-4级', 'aqi_status': '良', 'aqi_index': '89', 'aqi_rank': '340', 'pm25': '65', 'pm10': '101', 'so2': '7', 'no2': '39', 'co': '0.88', 'o3': '79'}, {'id': 74, 'city': '北京', 'weather_date': '2021-04-11', 'weather': '多云/多云', 'temperature': '21℃/11℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '83', 'aqi_rank': '343', 'pm25': '59', 'pm10': '95', 'so2': '3', 'no2': '34', 'co': '0.53', 'o3': '79'}, {'id': 75, 'city': '北京', 'weather_date': '2021-04-12', 'weather': '多云/晴', 'temperature': '20℃/8℃', 'wind': '北风3-4级/北风3-4级', 'aqi_status': '良', 'aqi_index': '74', 'aqi_rank': '307', 'pm25': '47', 'pm10': '73', 'so2': '3', 'no2': '31', 'co': '0.59', 'o3': '51'}, {'id': 76, 'city': '北京', 'weather_date': '2021-04-13', 'weather': '晴/晴', 'temperature': '17℃/5℃', 'wind': '西南风1-2级/西南风1-2级', 'aqi_status': '优', 'aqi_index': '30', 'aqi_rank': '76', 'pm25': '5', 'pm10': '24', 'so2': '2', 'no2': '13', 'co': '0.22', 'o3': '74'}, {'id': 77, 'city': '北京', 'weather_date': '2021-04-14', 'weather': '晴/多云', 'temperature': '22℃/10℃', 'wind': '西南风3-4级/西南风3-4级', 'aqi_status': '良', 'aqi_index': '66', 'aqi_rank': '319', 'pm25': '23', 'pm10': '83', 'so2': '2', 'no2': '27', 'co': '0.30', 'o3': '57'}, {'id': 78, 'city': '北京', 'weather_date': '2021-04-15', 'weather': '扬沙/扬沙', 'temperature': '23℃/8℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '中度污染', 'aqi_index': '171', 'aqi_rank': '328', 'pm25': '69', 'pm10': '306', 'so2': '4', 'no2': '23', 'co': '0.40', 'o3': '67'}, {'id': 79, 'city': '北京', 'weather_date': '2021-04-16', 'weather': '晴/晴', 'temperature': '19℃/9℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '轻度污染', 'aqi_index': '111', 'aqi_rank': '270', 'pm25': '36', 'pm10': '172', 'so2': '2', 'no2': '8', 'co': '0.21', 'o3': '70'}, {'id': 80, 'city': '北京', 'weather_date': '2021-04-17', 'weather': '晴/晴', 'temperature': '20℃/5℃', 'wind': '西北风1-2级/西北风1-2级', 'aqi_status': '优', 'aqi_index': '34', 'aqi_rank': '54', 'pm25': '9', 'pm10': '33', 'so2': '2', 'no2': '13', 'co': '0.22', 'o3': '68'}, {'id': 81, 'city': '北京', 'weather_date': '2021-04-18', 'weather': '晴/晴', 'temperature': '24℃/10℃', 'wind': '西南风3-4级/西南风3-4级', 'aqi_status': '良', 'aqi_index': '64', 'aqi_rank': '206', 'pm25': '25', 'pm10': '78', 'so2': '3', 'no2': '32', 'co': '0.35', 'o3': '60'}, {'id': 82, 'city': '北京', 'weather_date': '2021-04-19', 'weather': '晴/多云', 'temperature': '28℃/15℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '90', 'aqi_rank': '351', 'pm25': '54', 'pm10': '131', 'so2': '3', 'no2': '39', 'co': '0.50', 'o3': '87'}, {'id': 83, 'city': '北京', 'weather_date': '2021-04-20', 'weather': '多云/多云', 'temperature': '26℃/13℃', 'wind': '南风3-4级/南风3-4级', 'aqi_status': '良', 'aqi_index': '87', 'aqi_rank': '344', 'pm25': '52', 'pm10': '125', 'so2': '3', 'no2': '38', 'co': '0.57', 'o3': '101'}, {'id': 84, 'city': '北京', 'weather_date': '2021-04-21', 'weather': '阴/小雨', 'temperature': '21℃/11℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '64', 'aqi_rank': '309', 'pm25': '39', 'pm10': '76', 'so2': '2', 'no2': '34', 'co': '0.55', 'o3': '83'}, {'id': 85, 'city': '北京', 'weather_date': '2021-04-22', 'weather': '小雨/多云', 'temperature': '18℃/9℃', 'wind': '东风1-2级/东风1-2级', 'aqi_status': '优', 'aqi_index': '47', 'aqi_rank': '166', 'pm25': '32', 'pm10': '42', 'so2': '2', 'no2': '26', 'co': '0.62', 'o3': '69'}, {'id': 86, 'city': '北京', 'weather_date': '2021-04-23', 'weather': '多云/多云', 'temperature': '22℃/12℃', 'wind': '东风1-2级/东风1-2级', 'aqi_status': '优', 'aqi_index': '46', 'aqi_rank': '153', 'pm25': '24', 'pm10': '37', 'so2': '2', 'no2': '21', 'co': '0.50', 'o3': '69'}, {'id': 87, 'city': '北京', 'weather_date': '2021-04-24', 'weather': '多云/多云', 'temperature': '22℃/13℃', 'wind': '东风1-2级/东风1-2级', 'aqi_status': '优', 'aqi_index': '41', 'aqi_rank': '158', 'pm25': '20', 'pm10': '41', 'so2': '2', 'no2': '20', 'co': '0.45', 'o3': '79'}, {'id': 88, 'city': '北京', 'weather_date': '2021-04-25', 'weather': '多云/阴', 'temperature': '20℃/10℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '56', 'aqi_rank': '296', 'pm25': '38', 'pm10': '58', 'so2': '2', 'no2': '26', 'co': '0.55', 'o3': '77'}, {'id': 89, 'city': '北京', 'weather_date': '2021-04-26', 'weather': '小雨/多云', 'temperature': '20℃/8℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '57', 'aqi_rank': '264', 'pm25': '36', 'pm10': '62', 'so2': '3', 'no2': '28', 'co': '0.49', 'o3': '76'}, {'id': 90, 'city': '北京', 'weather_date': '2021-04-27', 'weather': '扬沙/晴', 'temperature': '23℃/11℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '良', 'aqi_index': '80', 'aqi_rank': '273', 'pm25': '28', 'pm10': '108', 'so2': '2', 'no2': '19', 'co': '0.35', 'o3': '70'}, {'id': 91, 'city': '北京', 'weather_date': '2021-04-28', 'weather': '多云/多云', 'temperature': '23℃/11℃', 'wind': '西南风3-4级/西南风3-4级', 'aqi_status': '良', 'aqi_index': '57', 'aqi_rank': '193', 'pm25': '13', 'pm10': '64', 'so2': '2', 'no2': '16', 'co': '0.22', 'o3': '74'}, {'id': 92, 'city': '北京', 'weather_date': '2021-04-29', 'weather': '晴/多云', 'temperature': '22℃/8℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '良', 'aqi_index': '56', 'aqi_rank': '181', 'pm25': '16', 'pm10': '66', 'so2': '2', 'no2': '20', 'co': '0.26', 'o3': '67'}, {'id': 93, 'city': '北京', 'weather_date': '2021-04-30', 'weather': '小雨/晴', 'temperature': '16℃/7℃', 'wind': '北风1-2级/北风1-2级', 'aqi_status': '优', 'aqi_index': '32', 'aqi_rank': '35', 'pm25': '12', 'pm10': '30', 'so2': '2', 'no2': '23', 'co': '0.30', 'o3': '59'}, {'id': 1, 'city': '北京', 'weather_date': '2021-05-01', 'weather': '晴/晴', 'temperature': '22℃/8℃', 'wind': '北风3-4级/北风3-4级', 'aqi_status': '优', 'aqi_index': '29', 'aqi_rank': '13', 'pm25': '9', 'pm10': '29', 'so2': '2', 'no2': '16', 'co': '0.25', 'o3': '56'}, {'id': 2, 'city': '北京', 'weather_date': '2021-05-02', 'weather': '晴/晴', 'temperature': '22℃/13℃', 'wind': '南风3-4级/南风3-4级', 'aqi_status': '优', 'aqi_index': '41', 'aqi_rank': '95', 'pm25': '12', 'pm10': '43', 'so2': '2', 'no2': '17', 'co': '0.25', 'o3': '67'}, {'id': 3, 'city': '北京', 'weather_date': '2021-05-03', 'weather': '多云/多云', 'temperature': '24℃/13℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '65', 'aqi_rank': '299', 'pm25': '35', 'pm10': '78', 'so2': '4', 'no2': '24', 'co': '0.49', 'o3': '88'}, {'id': 4, 'city': '北京', 'weather_date': '2021-05-04', 'weather': '多云/晴', 'temperature': '24℃/10℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '良', 'aqi_index': '54', 'aqi_rank': '222', 'pm25': '13', 'pm10': '63', 'so2': '2', 'no2': '11', 'co': '0.24', 'o3': '80'}, {'id': 5, 'city': '北京', 'weather_date': '2021-05-05', 'weather': '晴/晴', 'temperature': '27℃/15℃', 'wind': '西南风3-4级/西南风3-4级', 'aqi_status': '良', 'aqi_index': '74', 'aqi_rank': '276', 'pm25': '26', 'pm10': '99', 'so2': '2', 'no2': '18', 'co': '0.30', 'o3': '82'}, {'id': 6, 'city': '北京', 'weather_date': '2021-05-06', 'weather': '扬沙/多云', 'temperature': '28℃/14℃', 'wind': '西北风4-5级/西北风4-5级', 'aqi_status': '中度污染', 'aqi_index': '200', 'aqi_rank': '342', 'pm25': '82', 'pm10': '339', 'so2': '3', 'no2': '17', 'co': '0.84', 'o3': '81'}, {'id': 7, 'city': '北京', 'weather_date': '2021-05-07', 'weather': '晴/晴', 'temperature': '26℃/16℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '轻度污染', 'aqi_index': '142', 'aqi_rank': '254', 'pm25': '72', 'pm10': '215', 'so2': '2', 'no2': '8', 'co': '0.25', 'o3': '81'}, {'id': 8, 'city': '北京', 'weather_date': '2021-05-08', 'weather': '多云/多云', 'temperature': '26℃/12℃', 'wind': '西北风3-4级/西北风3-4级', 'aqi_status': '良', 'aqi_index': '95', 'aqi_rank': '253', 'pm25': '44', 'pm10': '130', 'so2': '2', 'no2': '16', 'co': '0.25', 'o3': '72'}, {'id': 9, 'city': '北京', 'weather_date': '2021-05-09', 'weather': '多云/多云', 'temperature': '26℃/13℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '良', 'aqi_index': '52', 'aqi_rank': '199', 'pm25': '20', 'pm10': '54', 'so2': '3', 'no2': '30', 'co': '0.37', 'o3': '72'}, {'id': 10, 'city': '北京', 'weather_date': '2021-05-10', 'weather': '多云/晴', 'temperature': '25℃/12℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '良', 'aqi_index': '52', 'aqi_rank': '225', 'pm25': '21', 'pm10': '56', 'so2': '3', 'no2': '27', 'co': '0.48', 'o3': '89'}]





class getDaysData(object):
    def __init__(self, data):
        #获取最近10天的数据进行DataFrame格式转化
        self.data = DataFrame(data).head(10)
        #日期数据转列表
        self.weather_date = self.data['weather_date'].tolist()
        #温度数据转列表
        self.temperature = self.data['temperature'].tolist()
        #风力数据转列表
        self.wind = self.data['wind'].tolist()
        #空气指数数据转列表
        self.tenDayAqiindex = self.data['aqi_index'].tolist()
        #pm2.5指数数据转列表
        self.tenDayPm25 = self.data['pm25'].tolist()
        #天气状况数据转列表
        self.weather = self.data['weather'].tolist()
        #空气状况数据转列表
        self.aqiStatuslist = self.data['aqi_status'].tolist()
    #对获取的白天的温度数据进行处理
    def getTenDaysTemp(self):
        self.tenDaysTemp = [t.split('/')[0].replace('℃', '') for t in self.temperature]
        return self.tenDaysTemp
    #对获取的夜晚的温度数据进行处理
    def getTenNightTemp(self):
        self.tenNightTemp = [t.split('/')[1].replace('℃', '') for t in self.temperature]
        return self.tenNightTemp
    #对获取的白天的风力数据进行处理
    def getTenDayWind(self):
        self.tenDayWind = [t.split('/')[0][-2:-1] for t in self.wind]
        return self.tenDayWind
    #对获取的夜晚的风力数据进行处理
    def getTenNightWind(self):
        self.tenNightWind = [t.split('/')[0][-2:-1] for t in self.wind]
        return self.tenNightWind
    #对获取的天气状况数据进行处理
    def getTenWeather(self):
        tenDayWeatherlist = [t.split('/')[0] for t in self.weather]
        tenDayWeathercounter = Counter(tenDayWeatherlist)
        self.tenDayWeather = [[k, v] for k, v in tenDayWeathercounter.items()]
        return self.tenDayWeather
    #对获取的空气状况数据进行处理
    def getTenAqiStatus(self):
        tenDayAqiStatus = Counter(self.aqiStatuslist)
        self.tenDayAqiStatus = [[k, v] for k, v in tenDayAqiStatus.items()]
        return self.tenDayAqiStatus
    #对获取的温度数据进行处理
    def tendTempBar(self):
        self.tenDTemp = (
            Bar(init_opts=opts.InitOpts(width="100%"))
                .add_xaxis(self.weather_date)
                .add_yaxis("白天", self.getTenDaysTemp())
                .add_yaxis("黑夜", self.getTenNightTemp())
                .set_global_opts(title_opts=opts.TitleOpts(title="最近10日温度柱状图", subtitle=""))
        )
        return self.tenDTemp

    def tendWindBar(self):
        self.tenDWind= (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(self.weather_date)
            .add_yaxis("白天", self.getTenDayWind())
            .add_yaxis("黑夜", self.getTenNightWind())
            .set_global_opts(title_opts=opts.TitleOpts(title="最近10日风力柱状图", subtitle=""))
    )
        return self.tenDWind

    def tendaqiBar(self):
        self.tendaqi = (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(self.weather_date)
            .add_yaxis("空气质量指数", self.tenDayAqiindex)
            .set_global_opts(title_opts=opts.TitleOpts(title="最近10日空气质量指数柱状图", subtitle=""))
    )
        return self.tendaqi
    def tendpm25Bar(self):
        self.tendpm25 = (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(self.weather_date)
            .add_yaxis("PM2.5值", self.tenDayPm25)
            .set_global_opts(title_opts=opts.TitleOpts(title="最近10日PM2.5值柱状图", subtitle=""))
    )
        return self.tendpm25
    def tendWeatherPie(self):
        self.tendWeatherPie = (
        Pie(init_opts=opts.InitOpts(width="100%"))
            .add("", self.getTenWeather())
            .set_global_opts(title_opts=opts.TitleOpts(title="最近10日天气分布饼状图"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
        return self.tendWeatherPie
    def tendAqiStatusPie(self):
        self.tendAqiStatus = (
        Pie(init_opts=opts.InitOpts(width="100%"))
            .add("", self.getTenAqiStatus())
            .set_global_opts(title_opts=opts.TitleOpts(title="最近10日空气质量状态分布饼状图"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
                )
        return self.tendAqiStatus


class getMYData(object):
    # 对月、年级数据进行处理。需要对日期进行格式转化，对其他数据列聚合分组
    def __init__(self, data,datetype):
        data = DataFrame(data)
        if datetype == 'month':
            data['weather_date'] = pd.to_datetime(data['weather_date']).apply(lambda x: x.strftime("%Y-%m"))
            self.datedes = "月维度"
        else:
            data['weather_date'] = pd.to_datetime(data['weather_date']).apply(lambda x: x.strftime("%Y"))
            self.datedes = "年维度"
        # 先对基础数据进行数据清洗
        data['daytemp'] = data['temperature'].apply(lambda x: x.split('/')[0].replace('℃', ''))
        data['nighttemp'] = data['temperature'].apply(lambda x: x.split('/')[1].replace('℃', ''))
        data['daywind'] = data['wind'].apply(lambda x: x.split('/')[0][-2:-1].replace('风','1'))
        data['nightwind'] = data['wind'].apply(lambda x: x.split('/')[1][-2:-1].replace('风','1'))
        # 把数据进行整形格式转换
        data[['aqi_index', 'aqi_rank', 'pm25', 'daytemp', 'nighttemp', 'daywind', 'nightwind']] = data[
            ['aqi_index', 'aqi_rank', 'pm25', 'daytemp', 'nighttemp', 'daywind', 'nightwind']].astype(int)
        # 把统计数据特征频次
        tenMonthAqiStatus = data['aqi_status'].value_counts().to_dict()
        self.tenMonthAqiStatus = [[k, v] for k, v in tenMonthAqiStatus.items()]
        self.weather = data['weather'].tolist()
        # 以日期进行数据分组
        dataGrouped = data.groupby(Grouper(key='weather_date'))
        # 获取分组后的日期列表
        self.weather_date = [k for k, v in dataGrouped]
        # 对分组后的数据列取平均值
        self.tenAqiIndex = dataGrouped['aqi_index'].mean().round(decimals=1).tolist()
        self.tenAqiRank = dataGrouped['aqi_rank'].mean().round(decimals=1).tolist()
        self.tenpm25 = dataGrouped['pm25'].mean().round(decimals=1).tolist()
        self.tenDayTemp = dataGrouped['daytemp'].mean().round(decimals=1).tolist()
        self.tenNightTemp = dataGrouped['nighttemp'].mean().round(decimals=1).tolist()
        self.tenDayWind = dataGrouped['daywind'].mean().round(decimals=1).tolist()
        self.tenNightWind = dataGrouped['nightwind'].mean().round(decimals=1).tolist()


    def getTenWeather(self):
        tenMonthWeatherlist = [t.split('/')[0] for t in self.weather]
        tenMonthWeathercounter = Counter(tenMonthWeatherlist)
        self.tenMonthWeather = [[k, v] for k, v in tenMonthWeathercounter.items()]
        return self.tenMonthWeather


    def tenTempBar(self):
        print(self.weather_date)
        print(self.tenDayTemp)
        print(self.tenNightTemp)
        self.tenMTemp = (
            Bar(init_opts=opts.InitOpts(width="100%"))
                .add_xaxis(self.weather_date)
                .add_yaxis("白天", self.tenDayTemp)
                .add_yaxis("黑夜", self.tenNightTemp)
                .set_global_opts(title_opts=opts.TitleOpts(title=f"{self.datedes}温度柱状图", subtitle=""))
        )
        return self.tenMTemp
    def tenWindBar(self):
        self.tenMDWind= (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(self.weather_date)
            .add_yaxis("白天", self.tenDayWind)
            .add_yaxis("黑夜", self.tenNightWind)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{self.datedes}风力柱状图", subtitle=""))
    )
        return self.tenMDWind
    def tenAqiBar(self):
        self.tenmaqi = (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(self.weather_date)
            .add_yaxis("空气质量指数", self.tenAqiIndex)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{self.datedes}空气质量指数柱状图", subtitle=""))
    )
        return self.tenmaqi
    def tenPm25Bar(self):
        self.tenmpm25 = (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(self.weather_date)
            .add_yaxis("PM2.5值", self.tenpm25)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{self.datedes}PM2.5值柱状图", subtitle=""))
    )
        return self.tenmpm25
    def tenWeatherPie(self):
        self.tendWeatherPie = (
        Pie(init_opts=opts.InitOpts(width="100%"))
            .add("", self.getTenWeather())
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{self.datedes}天气分布饼状图"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
        return self.tendWeatherPie
    def tenAqiStatusPie(self):
        self.tendAqiStatus = (
        Pie(init_opts=opts.InitOpts(width="100%"))
            .add("", self.tenMonthAqiStatus)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{self.datedes}空气质量状态分布饼状图"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
                )
        return self.tendAqiStatus



class cityWeatherAnalysis(object):
    def __init__(self, data):
        self.title = '郑州市 '+data[0]['weather_date'][:-3].replace('-','年')+'月'
        self.tmp_data = DataFrame(data)['weather'].tolist()
        self.aqi_data = DataFrame(data)['aqi_status'].tolist()
        tmp_data_count = Counter([t.split('/')[0] for t in self.tmp_data])
        self.result = [[k, v] for k, v in tmp_data_count.items()]

    def WeatherPie(self):
        self.tendWeatherPie = (
        Pie(init_opts=opts.InitOpts(width="100%"))
            .add("", self.result)
            .set_global_opts(title_opts=opts.TitleOpts(title=self.title))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
        return self.tendWeatherPie

    def rain_counter(self):
        rain_counter = len([i for i in self.tmp_data if '雨' in i])
        return rain_counter

    def aqi_counter(self):
        aqi_counter = len([i for i in self.aqi_data if '优' in i])
        return aqi_counter





def home(request):
    menu = ['日度分析','月度分析','年度分析']
    return render(request, 'home.html', {"menu":menu})

# 天维度数据展示
def days_show(request):
    data = getData('days')
    data = DataFrame(data)
    daysData = getDaysData(data)
    tenDayTempBar = daysData.tendTempBar()
    tenDayaqiBar = daysData.tendaqiBar()
    tenDaypm25Bar = daysData.tendpm25Bar()
    tenDayWeatherPie = daysData.tendWeatherPie()
    tenDayAqiStatusPie = daysData.tendAqiStatusPie()
    tenDayWindBar = daysData.tendWindBar()
    #以页模式渲染pyechart
    grid = (Page(layout=Page.SimplePageLayout).add(tenDayTempBar,tenDayaqiBar,tenDaypm25Bar,tenDayWindBar, tenDayWeatherPie, tenDayAqiStatusPie))
    return HttpResponse(grid.render_embed())

# 月维度数据展示
def months_show(request):
    data = getData('months')
    data = DataFrame(data)
    datetype = 'month'
    monthsData = getMYData(data,datetype)
    tenMonthTempBar = monthsData.tenTempBar()
    tenMonthWindBar = monthsData.tenWindBar()
    tenMonthaqiBar = monthsData.tenAqiBar()
    tenMonthpm25Bar = monthsData.tenPm25Bar()
    tenMonthWeatherPie = monthsData.tenWeatherPie()
    tenMonthAqiStatusPie = monthsData.tenAqiStatusPie()
    grid = (Page(layout=Page.SimplePageLayout).add(tenMonthTempBar,tenMonthWindBar,tenMonthaqiBar,tenMonthpm25Bar,tenMonthWeatherPie,tenMonthAqiStatusPie))
    return HttpResponse(grid.render_embed())

# 年维度数据展示
def years_show(request):

    data = getData('years')
    data = DataFrame(data)

    datetype = 'year'
    yearsData = getMYData(data,datetype)
    print('xxxxxxxxxxxxxxxxx')
    print(yearsData)
    yearsDataTempBar = yearsData.tenTempBar()
    yearsDataWindBar = yearsData.tenWindBar()
    yearsDataaqiBar = yearsData.tenAqiBar()
    yearsDatapm25Bar = yearsData.tenPm25Bar()
    yearsDataWeatherPie = yearsData.tenWeatherPie()
    yearsDataAqiStatusPie = yearsData.tenAqiStatusPie()
    grid = (Page(layout=Page.SimplePageLayout).add(yearsDataTempBar,yearsDataWindBar,yearsDataaqiBar,yearsDatapm25Bar,yearsDataWeatherPie,yearsDataAqiStatusPie))
    return HttpResponse(grid.render_embed())



def zz_weather_analysis(request):
    zz_17_sql = """SELECT weather_date,weather,aqi_status FROM `weather_original_tab` where weather_date >= '2017-07-01' and weather_date < '2017-08-01' and city = '郑州'"""
    zz_18_sql = """SELECT weather_date,weather,aqi_status FROM `weather_original_tab` where weather_date >= '2018-07-01' and weather_date < '2018-08-01' and city = '郑州'"""
    zz_19_sql = """SELECT weather_date,weather,aqi_status FROM `weather_original_tab` where weather_date >= '2019-07-01' and weather_date < '2019-08-01' and city = '郑州'"""
    zz_20_sql = """SELECT weather_date,weather,aqi_status FROM `weather_original_tab` where weather_date >= '2020-07-01' and weather_date < '2020-08-01' and city = '郑州'"""
    zz_21_sql = """SELECT weather_date,weather,aqi_status FROM `weather_original_tab` where weather_date >= '2021-07-01' and weather_date < '2021-08-01' and city = '郑州'"""
    zz_17_data = db.sqlselect(zz_17_sql,dict_mark=True)
    zz_18_data = db.sqlselect(zz_18_sql,dict_mark=True)
    zz_19_data = db.sqlselect(zz_19_sql,dict_mark=True)
    zz_20_data = db.sqlselect(zz_20_sql,dict_mark=True)
    zz_21_data = db.sqlselect(zz_21_sql,dict_mark=True)
    zz_17_pie = cityWeatherAnalysis(zz_17_data).WeatherPie()
    zz_18_pie = cityWeatherAnalysis(zz_18_data).WeatherPie()
    zz_19_pie = cityWeatherAnalysis(zz_19_data).WeatherPie()
    zz_20_pie = cityWeatherAnalysis(zz_20_data).WeatherPie()
    zz_21_pie = cityWeatherAnalysis(zz_21_data).WeatherPie()

    zz_17_rain = cityWeatherAnalysis(zz_17_data).rain_counter()
    zz_18_rain = cityWeatherAnalysis(zz_18_data).rain_counter()
    zz_19_rain = cityWeatherAnalysis(zz_19_data).rain_counter()
    zz_20_rain = cityWeatherAnalysis(zz_20_data).rain_counter()
    zz_21_rain = cityWeatherAnalysis(zz_21_data).rain_counter()

    zz_17_aqi = cityWeatherAnalysis(zz_17_data).aqi_counter()
    zz_18_aqi = cityWeatherAnalysis(zz_18_data).aqi_counter()
    zz_19_aqi = cityWeatherAnalysis(zz_19_data).aqi_counter()
    zz_20_aqi = cityWeatherAnalysis(zz_20_data).aqi_counter()
    zz_21_aqi = cityWeatherAnalysis(zz_21_data).aqi_counter()

    rainList = [zz_17_rain,zz_18_rain,zz_19_rain,zz_20_rain,zz_21_rain]
    aqiList = [zz_17_aqi,zz_18_aqi,zz_19_aqi,zz_20_aqi,zz_21_aqi]


    zzRainCounter = (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(['2017-07', '2018-07', '2019-07', '2020-07', '2021-07'])
            .add_yaxis("雨", rainList)
            .add_yaxis("优", aqiList)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"郑州7月份雨天/空气质量柱状图", subtitle=""))
    )


    grid = (Page(layout=Page.SimplePageLayout).add(zz_17_pie,zz_18_pie,zz_19_pie,zz_20_pie,zz_21_pie,zzRainCounter))
    return HttpResponse(grid.render_embed())