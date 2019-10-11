from django.shortcuts import render
from django.http import HttpResponse

def user_logout(request):
    return render(request, 'armageddon_system/user/logout.html')