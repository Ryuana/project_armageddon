from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/login', views.login.user_login, name='user/login'),
    path('user/logout', views.logout.user_logout, name='user/logout'),
    path('register/form',views.form.register_form,name='register/form'),
    path('register/confirm',views.confirm.register_confirm,name='register/confirm'),
    path('register/linepay',views.confirm.linepay_confirm, name='register/linepay.confirm')
]
