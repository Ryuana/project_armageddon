from django.shortcuts import render
from armageddon_system.models.dynamo_manager import DynamoManager as db
import qrcode

def log(request):

    dbm = db()
    context = {}
    context['pay_logs'] = dbm.get_pay_log_all()

    return render(request, 'armageddon_system/pay/log.html', context)

def item_list(request):

    dbm = db()
    context = {}
    context['forms'] = dbm.get_form_all()
    return render(request, 'armageddon_system/pay/item/list.html', context)

def item_qr(request,form):

    qr = form.qr
    img = qrcode.make(qr)
    img.save('qr_code.png')
    print(type(img))
    return render(request, 'armageddon_system/pay/item/qr.html',
                  {
                      'qr': qr,
                      'img': img,
                      'title': 'QR'
                  }
                  )