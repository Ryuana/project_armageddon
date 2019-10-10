from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/login', views.login.user_login, name='user/login'),
    path('user/logout', views.logout.user_logout, name='user/logout'),
]
