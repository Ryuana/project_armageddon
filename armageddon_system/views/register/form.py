from django.shortcuts import render, redirect
from django.http import HttpResponse
import armageddon_system.env as env
from armageddon_system.line_pay import LinePay
from armageddon_system.models.Transactions import Transactions

def register_form(request):
    return render(request, 'armageddon_system/register/form.html')