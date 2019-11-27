from django.shortcuts import render, HttpResponse
from armageddon_system.models import DynamoClass as dc
from armageddon_system.models import arrmagedon_models as model
from armageddon_system.models import dynamo_manager as db
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

    pom = dc.PayOffLogsModel()
    # pom_get = pom.scan()
    dbm = db.DynamoManager()
    pom_get = dbm.get_pay_log_all()
    context['pom_data'] = pom_get

    # pom_count = pom.count(hash_key=1)
    dbm = db.DynamoManager()
    pom_count = dbm.get_pay_log_count()

    context['pom_count'] = pom_count
    return render(request, 'armageddon_system/debug/testDynamo.html', context)


def add_pay_log(id):
    dbm = db.DynamoManager()
    import datetime
    # form_list = dbm.get_form_all()

    # dbm.save_pay_log(pay_log={'form_list': {"form":[form_list[0]]},
    #                           'isStudent':False,
    #                           # 'time_stamp':datetime.datetime.now()
    #                           'time_stamp':datetime.datetime.now()
    #                           },
    #                  )

    fm = model.Form(form_id=1,
                    form_name="申請書(仮)",
                    issuance_days=3,
                    fee=300,
                    qr="abcdefghijklmnopqrstuvwxyz")
    formlist = [{"form": fm, "quantity": 3}]
    paylog = model.PayLog(time_stamp=datetime.datetime.now(),
                          student_id=12345678,
                          school_id=12,
                          school_name="麻生情報",
                          course_id=34,
                          course_name="情報工学",
                          form_list=formlist
                          )
    dbm.save_pay_log(pay_log=paylog, id=id)


def delete_pay_log(id):
    dbm = db.DynamoManager()
    dbm.del_pay_log(id)


def paylog(request):
    context = {}
    dbm = db.DynamoManager()
    all_pay_log = dbm.get_pay_log_all()
    context['paylog'] = all_pay_log
    return render(request, 'armageddon_system/debug/dynamo_paylog.html', context)


def form(request):
    from armageddon_system import forms
    context = {}
    dbm = db.DynamoManager()

    if request.method == 'POST':
        form_item = forms.createformForm(request.POST)
        post_item = request.POST
        form_id = int(post_item['FORM_ID'])
        form_name = post_item['FORM_NAME']
        fee = post_item['FEE']
        qr = post_item['QR']
        issuance_days = post_item['ISSUANCE_DAYS']
        from armageddon_system.models import form
        new_form = form.Form(form_id=form_id, form_name=form_name, fee=fee, qr=qr, issuance_days=issuance_days)
        dbm.save_form(new_form)

    else:
        form_item = forms.createformForm()
    context['form'] = form_item
    context['all_form'] = dbm.get_form_all(is_ascending=True)
    return render(request, 'armageddon_system/debug/dynamo_form.html', context)
