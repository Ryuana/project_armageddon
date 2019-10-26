# from django.shortcuts import render
# from django.http import HttpResponse
# from armageddon_system.line_pay import LinePay
# import armageddon_system.env as env
# from armageddon_system.models import model
#
# LINE_PAY_URL = env.LINE_PAY_URL
# LINE_PAY_CHANNEL_ID = env.LINE_PAY_CHANNEL_ID
# LINE_PAY_CHANNEL_SECRET = env.LINE_PAY_CHANNEL_SECRET
# LINE_PAY_CONFIRM_URL = env.LINE_PAY_CONFIRM_URL
# app = __name__
# pay = LinePay(channel_id=LINE_PAY_CHANNEL_ID, channel_secret=LINE_PAY_CHANNEL_SECRET,
#               line_pay_url=LINE_PAY_URL, confirm_url=LINE_PAY_CONFIRM_URL)
#
#
# def index(request):
#     db = dynamodb_model.dynamo.get(hash_key="armageddon",range_key=1)
#     db_values = db.attribute_values
#     return render(request, 'armageddon_system/index.html',{'msg':db_values.get("Forms")[0]})
#
# def firm(request):
#     return render(request,'armageddon_system/register/form.html')
#
# def confirm(request):
#     if request.method == 'POST':
#         product_name = "チョコレート"
#         amount = 1
#         currency = "JPY"
#
#         (order_id, response) = pay.request_payments(product_name=product_name, amount=amount, currency=currency)
#         print(response["returnCode"])
#         print(response["returnMessage"])
#
#         transaction_id = response["info"]["transactionId"]
#         print(order_id, transaction_id, product_name, amount, currency)
#         obj = Transactions(transaction_id=transaction_id, order_id=order_id,
#                            product_name=product_name, amount=amount, currency=currency)
#         db.session.add(obj)
#         db.session.commit()
#         db.session.close()
#         redirect_url = response["info"]["paymentUrl"]["web"]
#         return redirect(redirect_url)
#     return render(request,'armageddon_system/register/confirm.html')