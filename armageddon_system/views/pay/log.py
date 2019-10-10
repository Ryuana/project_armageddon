from django.shortcuts import render
from django.http import HttpResponse

def pay_log(request):
    return render(request, 'armageddon_system/pay/log.html')