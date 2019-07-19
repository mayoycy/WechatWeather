import requests
import json
import datetime

def get_weather(city):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='
    url += city
    r = requests.get(url)
    data = json.loads(r.text)
    time_now = datetime.datetime.now()
    if time_now.hour >= 18 or time_now.hour <= 8:
        data = data['data']['forecast'][0]
    else:
        data = data['data']['forecast'][1]
    return data
