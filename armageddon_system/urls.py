from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/login', views.login, name='login'),
]
