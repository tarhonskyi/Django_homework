from django.urls import path
from .views import hello

urlpatterns = [
    path('hello_world/', hello, name='hello_world'),
]
