from django.shortcuts import render
from django.http import HttpResponse

def menu_item(request):
    return render(request, 'armageddon_system/menu/item.html')

def logout(request):
    request.session.clear()
    return render(request, 'armageddon_system/user/login.html')