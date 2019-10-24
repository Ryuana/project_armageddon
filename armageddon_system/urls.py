from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.user.login, name='login'),
    path('user/logout', views.user.logout, name='logout'),
    path('register/confirm', views.register.confirm, name='confirm'),
    path('register/form', views.register.form, name='form'),
    path('pay/item/list', views.pay.item_list, name='item_list'),
    path('pay/item/qr', views.pay.item_qr, name='item_qr'),
    path('pay/log', views.pay.log, name='pay_log'),
    path('menu/item', views.menu.menu_item, name='menu_item'),
    path('linebot/qa/list', views.linebot.qa_list, name='qa_list'),
    path('linebot/msg/edit', views.linebot.msg_edit, name='msg_edit'),
    path('linebot/msg/list', views.linebot.msg_list, name='msg_list'),

    path('debug', views.debug.debug, name='debug'),
    path('', views.debug.debug, name='debug'),
    path('debug/dynamo', views.debug.dynamo, name='debug_dynamo'),

]
