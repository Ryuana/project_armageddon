from django.shortcuts import render
from django.http import HttpResponse

def confirm(request):
    return render(request, 'armageddon_system/register/confirm.html')

def form(request):
    return render(request, 'armageddon_system/register/form.html')