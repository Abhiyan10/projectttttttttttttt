from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('bluetooth', views.bluetooth, name= 'bluetooth'),
    path('about', views.about, name='about' ),
    path('refresh', views.refresh, name='refresh'),    
] 
