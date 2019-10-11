from django.shortcuts import render
from django.http import HttpResponse

def menu_item(request):
    return render(request, 'armageddon_system/menu/item.html')