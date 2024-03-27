from django.shortcuts import render
import requests

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=66ad99905eeff16da429576520a894d7'

    city = 'Madrid'

    r = requests.get(url.format(city)).json()

    name = r['name']
    main = r['weather'][0]['main']
    description = r['weather'][0]['description']
    icon = r['weather'][0]['icon']
    temp = str(r['main']['temp']) + ' F'

    context = {'name':name, 'main':main, 'description':description, 'icon':icon, 'temp':temp,}
    print(context)

    return render(request, 'weather/weather.html', context)
