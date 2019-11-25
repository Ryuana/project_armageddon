from django.shortcuts import render
from armageddon_system.models.dynamo_manager import DynamoManager as db
import qrcode

def log(request):

    dbm = db()
    context = {}
    context['pay_logs'], context['total'] = dbm.get_pay_log_all()

    return render(request, 'armageddon_system/pay/log.html', context)

def item_list(request):

    dbm = db()
    context = {}
    context['forms'] = dbm.get_form_all()
    #context['count'] = 1
    #{{forms.0.form_id}}でjs取得可能

    return render(request, 'armageddon_system/pay/item/list.html', context)

def item_qr(request):

    context = {}
    context['form_name'] = request.POST['txt1']
    context['form_fee'] = request.POST['txt2']
    img = qrcode.make(request.POST['txt1'])
    img.save('armageddon_system/static/armageddon_system/qr_code.png')

    return render(request, 'armageddon_system/pay/item/qr.html', context)
