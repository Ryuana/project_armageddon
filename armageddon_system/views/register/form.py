from django.shortcuts import render
from django.http import HttpResponse

def register_form(request):
    return render(request, 'armageddon_system/register/form.html')