from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
# api key for weather ---- a2a165bc1dda30542a82e1e2cf79eb3e

def weather(request):
    appid = "a2a165bc1dda30542a82e1e2cf79eb3e"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        temp = data['main']['temp']
    except Exception as e:
        print("Exception (weather):", e)
        pass
    return render(request, 'weathermoney/weather.html',{
            'temp': '{}'.format(temp),
            'title': 'weather',
        })


def currency(request):
    response = requests.get('https://api.fixer.io/latest?base=RUB&symbols=USD,EUR')
    response_string = response.text
    parsed_json = json.loads(response_string)
    date = parsed_json['date']
    eur = parsed_json['rates']['EUR']
    usd = parsed_json['rates']['USD']
    return render(request, 'weathermoney/currency.html',{
        'eur': '{}'.format(eur),
        'usd': '{}'.format(usd),
        'date': '{}'.format(date),
        'title': 'currency',

    })
    # return HttpResponse(response.text)
