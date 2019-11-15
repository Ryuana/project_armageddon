from django.shortcuts import render
from armageddon_system.views import pay
from django.http import HttpResponse

def login(request):

    if request.method == 'GET':
        return render(request, 'armageddon_system/user/login.html')
    elif request.method == 'POST':
        is_login_success = False

        if 'ID' in request.POST and 'pass' in request.POST:
            request.session['user_id'] = request.POST['ID']
            request.session['user_pass'] = request.POST['pass']
            is_login_success = True
            #session_saveメソッドを作る

        if is_login_success:
            return pay.log(request)
            # return render(request, 'armageddon_system/pay/log.html')
        else:
            return render(request, 'armageddon_system/user/login.html')

def logout(request):

    request.session.clear()

    return render(request, 'armageddon_system/user/login.html')