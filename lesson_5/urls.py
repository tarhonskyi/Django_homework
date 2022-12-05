from django.urls import path
from . import views


app_name = 'lesson_5'

urlpatterns = [
    path('', views.index, name="index"),
    path('search_author/', views.search_author, name="search_author"),

]