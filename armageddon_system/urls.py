from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.user.login, name='login'),
    path('user/logout', views.user.logout, name='logout'),
    path('pay/item/list', views.pay.item_list, name='item_list'),
    path('pay/item/qr', views.pay.item_qr, name='item_qr'),
    path('pay/log', views.pay.log, name='pay_log'),
    path('menu/item', views.menu.menu_item, name='menu_item'),
    path('linebot/qa/list', views.linebot.qa_list, name='qa_list'),
    path('linebot/msg/edit', views.linebot.msg_edit, name='msg_edit'),
    path('linebot/msg/list', views.linebot.msg_list, name='msg_list'),

    # path('accounts/', include('django.contrib.auth.urls'))

    # LINE PAY #
    path('register/confirm', views.register.register_confirm, name='confirm'),
    path('register/form', views.register.register_form, name='form'),
    path('register/linepay', views.register.linepay_confirm, name='linepay.confirm'),

    # デバッグ用 #
    path('debug', views.debug.debug, name='debug'),
    path('', views.debug.debug, name='debug'),
    path('debug/dynamo', views.debug.dynamo, name='debug_dynamo'),
    path('debug/dynamo/paylog', views.debug.paylog, name='debug_dynamo_paylog'),
    path('debug/dynamo/form', views.debug.form, name='debug_dynamo_form'),

]
