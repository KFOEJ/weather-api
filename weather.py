import requests
from pprint import pprint

apiKey='134495f88f0d75736ddf5fed2aa60419'

city=input('Enter your city: ')

callUrl='api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+apiKey