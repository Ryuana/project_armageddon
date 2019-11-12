from django.shortcuts import render
from armageddon_system.models.dynamo_manager import DynamoManager as db
from armageddon_system.models.pay_log import PayLog
from django.http import HttpResponse

def display_pay_logs(request):

    pay_logs: PayLog = db.get_pay_log_all()
    print(pay_logs)

    return render(request, 'armageddon_system/pay/log.html', {'pay_logs': pay_logs})

def export_pay_logs(request, pay_logs: PayLog):

    """
    CSV出力処理
    """

    return HttpResponse()