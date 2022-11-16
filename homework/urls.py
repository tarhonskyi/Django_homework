"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home, book, index, bio

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$|^home/', home, name='home-view'),
    path('index/', index, name='index-view'),
    path('bio/<str:user_name>/', bio, name='bio'),
    path('book/<str:title>/', book, name='book'),
    path('lesson_1/', include('lesson_1.urls')),
    path('lesson_2/', include('lesson_2.urls')),
    path('lesson_3/', include('lesson_3.urls')),
    path('lesson_4/', include('lesson_4.urls')),
]
