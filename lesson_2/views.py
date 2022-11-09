from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .weather import get_weather_info


def index(request):
    return HttpResponse('This is lesson_2 index page!')


def weather(request: HttpRequest, city: str) -> HttpResponse:
    template = 'lesson_2/weather.html'
    city_weather = get_weather_info(city)
    if city_weather['cod'] == '404':
        if city_weather['message'] == 'city not found':
            return HttpResponse(f'<script>alert("City {city} does not exist!");</script>')
    context = {'country': city_weather['sys']['country'],
               'city': city_weather['name'],
               'lon': city_weather['coord']['lon'],
               'lat': city_weather['coord']['lat'],
               'weather': (city_weather['weather'])[0]['main'],
               'temp': f"{city_weather['main']['temp'] - 273.15:.2f}",
               }
    return render(request, template_name=template, context=context)
