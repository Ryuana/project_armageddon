from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'armageddon_system/user/login.html')

def logout(request):
    return render(request, 'armageddon_system/user/logout.html')