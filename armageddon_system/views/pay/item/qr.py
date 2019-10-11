from django.shortcuts import render
from django.http import HttpResponse

def pay_item_qr(request):
    return render(request, 'armageddon_system/pay/item/qr.html')