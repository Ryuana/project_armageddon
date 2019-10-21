from django.shortcuts import render, redirect
from django.http import HttpResponse
import armageddon_system.env as env
from armageddon_system.line_pay import LinePay
from armageddon_system.models.Transactions import Transactions

LINE_PAY_URL = env.LINE_PAY_URL
LINE_PAY_CHANNEL_ID = env.LINE_PAY_CHANNEL_ID
LINE_PAY_CHANNEL_SECRET = env.LINE_PAY_CHANNEL_SECRET
LINE_PAY_CONFIRM_URL = env.LINE_PAY_CONFIRM_URL

pay = LinePay(channel_id=LINE_PAY_CHANNEL_ID, channel_secret=LINE_PAY_CHANNEL_SECRET,line_pay_url=LINE_PAY_URL, confirm_url=LINE_PAY_CONFIRM_URL)

def register_confirm(request):
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
    # db.session.add(obj)
    # db.session.commit()
    # db.session.close()
    redirect_url = response["info"]["paymentUrl"]["web"]
    return redirect(redirect_url)
    # return render(request, 'armageddon_system/register/confirm.html')

def linepay_confirm(request):
    transaction_id = request.args.get('transactionId')
    obj = Transactions.query.filter_by(transaction_id=transaction_id).one_or_none()
    if obj is None:
        raise Exception("Error: transaction_id not found.")

    response = pay.confirm_payments(transaction_id=transaction_id, amount=obj.amount, currency=obj.currency)
    print(response["returnCode"])
    print(response["returnMessage"])

    # db.session.query(Transactions).filter(Transactions.transaction_id == transaction_id).delete()
    # db.session.commit()
    # db.session.close()
    return "Payment successfully finished."