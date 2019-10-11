from django.shortcuts import render
from django.http import HttpResponse

def register_confirm(request):
    return render(request, 'armageddon_system/register/confirm.html')