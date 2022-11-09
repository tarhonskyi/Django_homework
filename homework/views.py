from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is index page!')


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("It is home-view")


def book(request: HttpRequest, title: str) -> HttpResponse:
    return HttpResponse(f"This is page for '{title}' book!")


def bio(request: HttpRequest, user_name: str) -> HttpResponse:
    return HttpResponse(f"<h1>Hello, {user_name.title()}!!!</h1>")
