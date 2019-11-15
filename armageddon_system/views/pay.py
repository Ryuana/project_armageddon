from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.models.dynamo_manager import DynamoManager as db
from armageddon_system.models.form import Form
from armageddon_system.models.pay_log import PayLog

def log(request):
    dbm = db()
    pay_logs = dbm.get_pay_log_all()
    a: Form
    for pay_log in pay_logs:
        for fm in pay_log.form_list:
            a = fm['form']
    return render(request, 'armageddon_system/pay/log.html')

#成功 forms[x番目].変数でデータ取得可能
def item_list(request):
    dbm = db()
    forms = dbm.get_form_all()
    print(forms[0].form_id)
    return render(request, 'armageddon_system/pay/item/list.html')

def item_qr(request):
    return render(request, 'armageddon_system/pay/item/qr.html')