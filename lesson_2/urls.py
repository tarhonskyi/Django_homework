from django.urls import path
from .views import weather


urlpatterns = [
    path('weather/<str:city>/', weather, name='city_weather'),
]
