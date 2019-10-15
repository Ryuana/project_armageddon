from django.shortcuts import render
from django.http import HttpResponse

def log(request):
    return render(request, 'armageddon_system/pay/log.html')

def item_list(request):
    return render(request, 'armageddon_system/pay/item/list.html')

def item_qr(request):
    return render(request, 'armageddon_system/pay/item/qr.html')