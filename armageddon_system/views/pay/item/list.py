from django.shortcuts import render
from django.http import HttpResponse

def pay_item_list(request):
    return render(request, 'armageddon_system/pay/item/list.html')