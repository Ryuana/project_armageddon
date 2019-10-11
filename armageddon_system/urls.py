from django.contrib import admin
from django.urls import path, include
import armageddon_system.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/form', views.form, name='form'),
    path('register/confirm',views.confirm,name='confirm')
]
