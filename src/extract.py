import requests
from datetime import datetime
import pandas as pd
import os

def extract():

    citys = {
        'city_one': {'lat': -12.9822499, 'lon': -38.4812772}, # Trancoso - BA.
        'city_two': {'lat': -22.9110137, 'lon': -43.2093727}, # Rio de Janeiro - RJ
        'city_three': {'lat': -1.4455024, 'lon': -48.48705957271403}, # Belém - PA
        'city_four': {'lat': -9.9765362, 'lon': -67.8220778}, # Rio Branco - AC
        'city_five': {'lat': 2.8208478, 'lon': -60.6719582} # Boa Vista - RR
    }

    datas_citys = {
        'name': [],
        'temperature': [],
        'humidity': [],
        'description': [],
        'collected_at': []
    }

    url = "https://api.openweathermap.org/data/2.5/weather"

    for city in citys:

        params = {
            'lat': citys[city]['lat'],
            'lon': citys[city]['lon'],
            'appid': os.getenv("API_KEY")
        }

        r = requests.get(url, params=params)

        if r.status_code == 200:
            datas = r.json()
            
            datas_citys['name'].append(datas['name'])
            datas_citys['temperature'].append(datas['main']['temp'])
            datas_citys['humidity'].append(datas['main']['humidity'])
            datas_citys['description'].append(datas['weather'][0]['description'])
            datas_citys['collected_at'].append(datetime.now())

    return pd.DataFrame(datas_citys)