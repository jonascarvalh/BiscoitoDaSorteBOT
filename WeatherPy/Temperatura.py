import requests, json
from WeatherPy.Queries import *
from WeatherPy.Url import *
from WeatherPy.IconFormat import *

def Temperatura(city):
    # Build Url
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = Url(Queries(city).getQueries(), base_url)
    url = url.getUrl()

    # HTTP Request
    response = requests.get(url)

    # Checking the status request
    if response.status_code == 200:
        data    = response.json()
        main    = data['main'] # Acessa inforemações de clima e tempo
        sys     = data['sys']  # Acessa informações de região
        weather = data['weather']

        temperature = main['temp']
        humidity    = main['humidity']
        pressure    = main['pressure']
        temp_min    = main['temp_min']
        temp_max    = main['temp_max']
        country     = sys['country']
        description = weather[0]['description']
        icon = weather[0]['icon']
        description = IconFormat(icon) + description
        #report = data['weather']

        return temperature,humidity,pressure,temp_min,temp_max,country,description
    else:
        print('Error in HTTP request!')

