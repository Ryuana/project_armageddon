from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.line_pay import LinePay
import armageddon_system.env as env

def index(request):
    return render(request, 'armageddon_system/index.html',{'msg':'test'})

def test(request):

    LINE_PAY_URL = 'https://sandbox-api-pay.line.me'
    LINE_PAY_CHANNEL_ID = 'your channel'
    LINE_PAY_CHANNEL_SECRET = 'your secret'
    LINE_PAY_CONFIRM_URL = 'http://localhost:8000/pay/confirm'
    pay = LinePay(channel_id=LINE_PAY_CHANNEL_ID, channel_secret=LINE_PAY_CHANNEL_SECRET,
                  line_pay_url=LINE_PAY_URL, confirm_url=LINE_PAY_CONFIRM_URL)

    if request.method == "POST":
        def index():
            return render(request,'index.html')
    else:
        product_name = "チョコレート"
        amount = 1
        currency = "JPY"
        (order_id, response) = pay.request_payments(product_name=product_name, amount=amount, currency=currency)
        print(response["returnCode"])
        print(response["returnMessage"])

        transaction_id = response["info"]["transactionId"]
        print(order_id, transaction_id, product_name, amount, currency)
        obj = Transactions(transaction_id=transaction_id, order_id=order_id,
                           product_name=product_name, amount=amount, currency=currency)
        db.session.add(obj)
        db.session.commit()
        db.session.close()
        redirect_url = response["info"]["paymentUrl"]["web"]
        return redirect_url(redirect_url)