from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='v_home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('personal', views.personal, name='personal'),
    path('medical', views.medical, name='medical'),
    path('document', views.document, name='document'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('search', views.search, name='search'),
    path('get_hospital', views.get_hospital, name='get_hospital'),
    path('book', views.book, name='book'),
]