from django.conf.urls import url

from weatherCrawler import dashboard

urlpatterns = [
    url(r'^days_show/', dashboard.days_show),
    url(r'^months_show/', dashboard.months_show),
    url(r'^years_show/', dashboard.years_show),
    url(r'^zz_weather_analysis/', dashboard.zz_weather_analysis),
    url(r'^', dashboard.days_show)]