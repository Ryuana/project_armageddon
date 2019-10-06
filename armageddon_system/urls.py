from django.contrib import admin
from django.urls import path, include
import armageddon_system.views as armageddon_system

urlpatterns = [
    path('/hello', armageddon_system.index),
    path('', armageddon_system.index),
]
