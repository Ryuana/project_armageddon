from django.contrib import admin
from django.urls import path, include
import armageddon_system.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='linepay')
]
