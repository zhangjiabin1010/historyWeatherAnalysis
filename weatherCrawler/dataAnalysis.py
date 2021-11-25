from collections import Counter

from weatherCrawler.db import db
from pandas.core.frame import DataFrame

def zz_data_analysis(data):
    tmp_data = DataFrame(data)['weather'].tolist()
    tmp_data_count = Counter([t.split('/')[0] for t in tmp_data])
    result = [[k, v] for k, v in tmp_data_count.items()]
    return result


def getzzData():
    zz_17_sql = """SELECT weather_date,weather FROM `weather_original_tab` where weather_date > '2017-07-01' and weather_date < '2017-08-01' and city = '郑州'"""
    zz_18_sql = """SELECT weather_date,weather FROM `weather_original_tab` where weather_date > '2018-07-01' and weather_date < '2018-08-01' and city = '郑州'"""
    zz_19_sql = """SELECT weather_date,weather FROM `weather_original_tab` where weather_date > '2019-07-01' and weather_date < '2019-08-01' and city = '郑州'"""
    zz_20_sql = """SELECT weather_date,weather FROM `weather_original_tab` where weather_date > '2020-07-01' and weather_date < '2020-08-01' and city = '郑州'"""
    zz_21_sql = """SELECT weather_date,weather FROM `weather_original_tab` where weather_date > '2021-07-01' and weather_date < '2021-08-01' and city = '郑州'"""
    zz_17_data = db.sqlselect(zz_17_sql,dict_mark=True)
    zz_18_data = db.sqlselect(zz_18_sql,dict_mark=True)
    zz_19_data = db.sqlselect(zz_19_sql,dict_mark=True)
    zz_20_data = db.sqlselect(zz_20_sql,dict_mark=True)
    zz_21_data = db.sqlselect(zz_21_sql,dict_mark=True)
    zz_17_pie_data = zz_data_analysis(zz_17_data)
    zz_18_pie_data = zz_data_analysis(zz_18_data)
    zz_19_pie_data = zz_data_analysis(zz_19_data)
    zz_20_pie_data = zz_data_analysis(zz_20_data)
    zz_21_pie_data = zz_data_analysis(zz_21_data)

    print(zz_17_pie_data)
    print(zz_18_pie_data)
    print(zz_19_pie_data)
    print(zz_20_pie_data)
    print(zz_21_pie_data)
if __name__ == '__main__':
    getzzData()
    # data = getData()
    # data = DataFrame(data)

    # data=[{'id': 63, 'city': '北京', 'weather_date': '2021-06-30', 'weather': '雷阵雨/阴', 'temperature': '32℃/23℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '优', 'aqi_index': '34', 'aqi_rank': '181', 'pm25': '13', 'pm10': '27', 'so2': '2', 'no2': '9', 'co': '0.53', 'o3': '108'}, {'id': 62, 'city': '北京', 'weather_date': '2021-06-29', 'weather': '雷阵雨/雷阵雨', 'temperature': '29℃/22℃', 'wind': '东北风1-2级/东北风1-2级', 'aqi_status': '优', 'aqi_index': '43', 'aqi_rank': '246', 'pm25': '26', 'pm10': '41', 'so2': '2', 'no2': '12', 'co': '0.65', 'o3': '95'}, {'id': 61, 'city': '北京', 'weather_date': '2021-06-28', 'weather': '雷阵雨/雷阵雨', 'temperature': '35℃/22℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '62', 'aqi_rank': '314', 'pm25': '32', 'pm10': '54', 'so2': '2', 'no2': '15', 'co': '0.80', 'o3': '126'}, {'id': 60, 'city': '北京', 'weather_date': '2021-06-27', 'weather': '多云/晴', 'temperature': '34℃/23℃', 'wind': '东风1-2级/东风1-2级', 'aqi_status': '良', 'aqi_index': '57', 'aqi_rank': '319', 'pm25': '25', 'pm10': '46', 'so2': '2', 'no2': '15', 'co': '0.73', 'o3': '113'}, {'id': 59, 'city': '北京', 'weather_date': '2021-06-26', 'weather': '雷阵雨/多云', 'temperature': '31℃/23℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '优', 'aqi_index': '40', 'aqi_rank': '230', 'pm25': '20', 'pm10': '37', 'so2': '2', 'no2': '13', 'co': '0.66', 'o3': '104'}, {'id': 58, 'city': '北京', 'weather_date': '2021-06-25', 'weather': '雷阵雨/多云', 'temperature': '28℃/22℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '优', 'aqi_index': '49', 'aqi_rank': '251', 'pm25': '31', 'pm10': '49', 'so2': '2', 'no2': '17', 'co': '0.84', 'o3': '99'}, {'id': 57, 'city': '北京', 'weather_date': '2021-06-24', 'weather': '小雨/小雨', 'temperature': '26℃/20℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '优', 'aqi_index': '43', 'aqi_rank': '174', 'pm25': '23', 'pm10': '44', 'so2': '2', 'no2': '24', 'co': '0.53', 'o3': '90'}, {'id': 56, 'city': '北京', 'weather_date': '2021-06-23', 'weather': '小雨/小雨', 'temperature': '32℃/22℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '优', 'aqi_index': '38', 'aqi_rank': '111', 'pm25': '18', 'pm10': '34', 'so2': '2', 'no2': '20', 'co': '0.44', 'o3': '78'}, {'id': 55, 'city': '北京', 'weather_date': '2021-06-22', 'weather': '多云/小雨', 'temperature': '33℃/20℃', 'wind': '南风1-2级/南风1-2级', 'aqi_status': '良', 'aqi_index': '53', 'aqi_rank': '231', 'pm25': '14', 'pm10': '43', 'so2': '2', 'no2': '16', 'co': '0.49', 'o3': '117'}, {'id': 54, 'city': '北京', 'weather_date': '2021-06-21', 'weather': '多云/多云', 'temperature': '35℃/21℃', 'wind': '东南风1-2级/东南风1-2级', 'aqi_status': '良', 'aqi_index': '63', 'aqi_rank': '289', 'pm25': '17', 'pm10': '65', 'so2': '3', 'no2': '24', 'co': '0.45', 'o3': '114'}]


