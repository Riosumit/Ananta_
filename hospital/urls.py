from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.home, name="h_home"),
    path('login', views.login, name="h_login"),
    path('logout', views.logout, name="h_logout"),
    path('upload_report', views.upload_report, name="upload_report"),
    path('search_volunteer', views.search_volunteer, name="search_volunteer"),
]