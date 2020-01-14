from django.shortcuts import render, redirect
from django.http import HttpResponse
import armageddon_system.env as env
from armageddon_system.line_pay import LinePay
from armageddon_system.models.dynamo_manager import DynamoManager as db
from armageddon_system.models import DynamoClass as dc
from armageddon_system.models import arrmagedon_models as am
import json

LINE_PAY_URL = env.LINE_PAY_URL
LINE_PAY_CHANNEL_ID = env.LINE_PAY_CHANNEL_ID
LINE_PAY_CHANNEL_SECRET = env.LINE_PAY_CHANNEL_SECRET
LINE_PAY_CONFIRM_URL = env.LINE_PAY_CONFIRM_URL

pay = LinePay(channel_id=LINE_PAY_CHANNEL_ID, channel_secret=LINE_PAY_CHANNEL_SECRET, line_pay_url=LINE_PAY_URL,
              confirm_url=LINE_PAY_CONFIRM_URL)


def register_form(request):
    context = {}
    form_list = db().get_form_all()
    context['forms'] = form_list
    form_dict = {}
    for i in form_list:
        form_map = {
            "form_id": i.form_id,
            "form_name": i.form_name,
            "fee": i.fee
        }
        form_dict[f"{i.qr}"] = form_map
    context['formDict'] = form_dict
    return render(request, 'armageddon_system/register/form.html', context)


def register_confirm(request):
    dbm = db()
    context = {}
    if request.POST.get('hasNotStudentId', False):
        context['student_id'] = request.POST['userName']
    else:
        context['student_id'] = request.POST['studentId']
    form_list = []
    total = 0
    for i in range(int(request.POST['countFormTypes'])):
        id = int(request.POST[f'form_id{i}'])
        name = request.POST[f'form_name{i}']
        count = int(request.POST[f'count{i}'])
        fee = int(request.POST[f'fee{i}'])
        subtotal = fee * count
        total += subtotal
        form_list.append({
            'id': id,
            'name': name,
            'count': count,
            'fee': fee,
            'subtotal': subtotal
        })
    context['is_multiple'] = [False, True][int(request.POST['countFormTypes']) > 1]
    context['countFormTypes'] = int(request.POST['countFormTypes'])
    context['form_list'] = form_list
    context['total'] = total

    return render(request, 'armageddon_system/register/confirm.html', context)


def payments(request):
    if request.POST['is_multiple'] == "True":
        form_name = "証明書(複数)"
    else:
        form_name = request.POST['form_name0']
    fee = int(request.POST['total'])
    (order_id, response) = pay.request_payments(product_name=form_name, amount=fee, currency="JPY",
                                                product_image_url="https://3.bp.blogspot.com/-5o2cwzzEJWI/Vz_w2t2PtXI/AAAAAAAA6uU/IOsMq7K2zjgOcldRuPmf09xXeQ2CnZTVACLcB/s800/document_syorui_pen.png")


    transaction_id = response["info"]["transactionId"]
    # obj = Transactions(transaction_id=transaction_id, order_id=order_id,
    #                    product_name=product_name, amount=amount, currency=currency)
    obj = dc.Transactions(str(transaction_id))
    obj.order_id = order_id
    obj.product_name = form_name
    obj.amount = fee
    obj.currency = "JPY"
    obj.save()

    import datetime
    date = datetime.datetime.now()
    student_id = request.POST['student_id']

    school_name = "-"
    course_name = "情報工学科"
    form_list = []

    for i in range(int(request.POST['countFormTypes'])):
        form_item = {
            'form_id': request.POST[f'form_id{i}'],
            'form_name': request.POST[f'form_name{i}'],
            'fee': request.POST[f'fee{i}'],
            'quantity': request.POST[f'form_count{i}']
        }
        form_list.append(form_item)
    paylog = am().PayLog(
        time_stamp=date,
        form_list=form_list,
        student_id=int(student_id)
    )

    db().save_pay_log(paylog)

    redirect_url = response["info"]["paymentUrl"]["web"]
    return redirect(redirect_url)


def linepay_confirm(request):
    transaction_id = request.GET.get('transactionId')
    obj = dc.Transactions.get(hash_key=transaction_id)

    if obj is None:
        raise Exception("Error: transaction_id not found.")

    response = pay.confirm_payments(transaction_id=transaction_id, amount=obj.amount, currency=obj.currency)

    return HttpResponse("Payment successfully finished.")
