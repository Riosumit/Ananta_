from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.home, name="a_home"),
    path('login', views.login, name="a_login"),
    path('logout', views.logout, name="a_logout"),
]