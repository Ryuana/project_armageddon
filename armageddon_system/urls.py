from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.user.login, name='login'),
    path('user/logout', views.user.logout, name='logout'),
    path('pay/item/list', views.pay.item_list, name='item_list'),
    path('pay/item/qr', views.pay.item_qr, name='item_qr'),
    path('pay/item/list/delete', views.pay.item_delete, name='item_delete'),
    path('pay/log', views.pay.log, name='log'),
    path('linebot/qa/list', views.linebot.display_qa_list, name='display_qa_list'),
    path('linebot/qa/save', views.linebot.save_qa, name='save_qa'),
    path('linebot/qa/delete', views.linebot.delete_qa, name='delete_qa'),
    path('linebot/msg/list', views.linebot.display_messages, name='msg_list'),
    path('linebot/msg/edit', views.linebot.edit_message, name='edit_message'),
    path('linebot/msg/save', views.linebot.save_message, name='save_message'),

    # path('accounts/', include('django.contrib.auth.urls'))

    # LINE PAY #
    path('register/confirm', views.register.register_confirm, name='confirm'),
    path('register/form', views.register.register_form, name='form'),
    path('register/linepay', views.register.payments, name='linepay.confirm'),

    # デバッグ用 #
    path('debug', views.debug.debug, name='debug'),
    path('', views.debug.debug, name='debug'),
    path('debug/dynamo', views.debug.dynamo, name='debug_dynamo'),
    path('debug/dynamo/paylog', views.debug.paylog, name='debug_dynamo_paylog'),
    path('debug/dynamo/form', views.debug.form, name='debug_dynamo_form'),

]
