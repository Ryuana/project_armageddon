from django.shortcuts import render
from django.http import HttpResponse
#from armageddon_system.models.session import Session as ss

def login(request, user_id = 0, user_pass = ""):
    """
        if request.method == 'POST':
        セッション管理クラスにID,Passを渡し、Trueが返ってきたら画面遷移
    """
    return render(request, 'armageddon_system/user/login.html')

def logout(request,user_id):
    """
    userIdを元にsession破棄
    """
    return render(request, 'armageddon_system/user/login.html')
