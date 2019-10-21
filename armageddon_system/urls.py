from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.user.login, name='user/login'),
    path('user/logout', views.user.logout, name='user/logout'),
    path('register/confirm', views.register.confirm, name='user/confirm'),
    path('register/form', views.register.form, name='user/form'),
    path('pay/item/list', views.pay.item_list, name='pay/item/list'),
    path('pay/item/qr', views.pay.item_qr, name='pay/item/qr'),
    path('pay/log', views.pay.log, name='pay/log'),
    path('menu/item', views.menu.menu_item, name='menu/item'),
    path('linebot/qa/list', views.linebot.qa_list, name='linebot/qa/list'),
    path('linebot/msg/edit', views.linebot.msg_edit, name='linebot/msg/edit'),
    path('linebot/msg/list', views.linebot.msg_list, name='linebot/msg/list'),

    path('accounts/', include('django.contrib.auth.urls'))
]
