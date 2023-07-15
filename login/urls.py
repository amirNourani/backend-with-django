from os import name
from django import views
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login')
]