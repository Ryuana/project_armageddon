from django.shortcuts import render, redirect
from django.http import HttpResponse
import armageddon_system.env as env
from armageddon_system.line_pay import LinePay
from armageddon_system.models.dynamo_manager import DynamoManager as db
from armageddon_system.models import DynamoClass as dc

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
    return render(request, 'armageddon_system/register/form.html', context)

def register_confirm(request):

    dbm = db()
    context = {}
    context['student_id'] = request.GET['student_id']
    context['form_list'] = request.GET['form_list']
    context['quantity'] = request.GET['quantity']

    # dbm.save_pay_log(context)

    return render(request, 'armageddon_system/register/confirm.html', context)




def payments(request):
    form_name = request.POST['form_name']
    fee = int(request.POST['fee'])
    (order_id, response) = pay.request_payments(product_name=form_name, amount=fee, currency="JPY")
    print(response["returnCode"])
    print(response["returnMessage"])

    transaction_id = response["info"]["transactionId"]
    print(order_id, transaction_id, form_name, fee, "JPY")
    # obj = Transactions(transaction_id=transaction_id, order_id=order_id,
    #                    product_name=product_name, amount=amount, currency=currency)
    obj = dc().Transactions(str(transaction_id))
    obj.order_id = order_id
    obj.product_name = form_name
    obj.amount = fee
    obj.currency = "JPY"
    obj.save()

    redirect_url = response["info"]["paymentUrl"]["web"]
    return redirect(redirect_url)

def linepay_confirm(request):
    transaction_id = request.GET.get('transactionId')
    obj = dc.Transactions.get(hash_key=transaction_id)

    if obj is None:
        raise Exception("Error: transaction_id not found.")

    response = pay.confirm_payments(transaction_id=transaction_id, amount=obj.amount, currency=obj.currency)
    print(response["returnCode"])
    print(response["returnMessage"])

    return HttpResponse("Payment successfully finished.")


