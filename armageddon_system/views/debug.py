from django.shortcuts import render, HttpResponse
from armageddon_system.models import DynamoManager as db
from armageddon_system.models import model
import json


def debug(request):
    return render(request, 'armageddon_system/debug/debug.html')


def dynamo(request):
    cmd = request.GET.get('cmd')
    context = {}
    id = request.GET.get('id')
    if id:
        id = int(id)
    context['cmd'] = cmd
    if cmd == "add_pay_log":
        add_pay_log(id)
    if cmd == "delete_pay_log":
        delete_pay_log(id)
    # dbm = db.DynamoManager()
    # pay_log = dbm.get_pay_log_all()
    # context = {'pay_log': pay_log}
    pom = model.PayOffLogsModel
    pom_get = pom.scan()
    context['pom_data'] = []
    for pom_item in pom_get:
        context['pom_data'].append(json.dumps(dict(pom_item)))

    # pom_count = pom.count(hash_key=1)
    dbm = db.DynamoManager()
    pom_count = dbm.get_pay_log_count()

    context['pom_count'] = pom_count
    return render(request, 'armageddon_system/debug/testDynamo.html', context)


def add_pay_log(id):
    dbm = db.DynamoManager()
    dbm.save_pay_log(id, "a")


def delete_pay_log(id):
    dbm = db.DynamoManager()
    dbm.del_pay_log(id)


def paylog(request):
    context = {}
    return render(request, 'armageddon_system/debug/dynamo_paylog.html', context)


def form(request):
    from armageddon_system import forms
    context = {}
    if request.method == 'POST':
        form_item = forms.createformForm(request.POST)
        form_id = form_item['FORM_ID']
        form_name = form_item['FORM_NAME']
        fee = form_item['FEE']
        qr = form_item['QR']
        from armageddon_system.models import form
        form.Form(form_id=form_id, form_name=form_name, fee=fee, qr=qr)


    else:
        form_item = forms.createformForm()
    context['form'] = form_item
    return render(request, 'armageddon_system/debug/dynamo_form.html', context)
