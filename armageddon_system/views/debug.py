from django.shortcuts import render
from armageddon_system.models import DynamoManager as db
from armageddon_system.models import model
import json


def debug(request):
    return render(request, 'armageddon_system/debug/debug.html')


def dynamo(request):
    cmd = request.GET.get('cmd')
    context = {}
    context['cmd'] = cmd
    if cmd == "add_pay_log":
        add_pay_log()
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

    context['pom_count'] = pom_count+1
    return render(request, 'armageddon_system/debug/testDynamo.html', context)


def add_pay_log():
    dbm = db.DynamoManager()
    dbm.save_pay_log("a")
