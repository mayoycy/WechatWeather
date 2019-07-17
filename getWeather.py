import requests
import json

def get_weather(city):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='
    url += city
    r = requests.get(url)
    data = json.loads(r.text)
    data = data['data']['forecast'][1]
    return data
