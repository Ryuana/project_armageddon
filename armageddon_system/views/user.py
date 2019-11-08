from django.shortcuts import render
from django.http import HttpResponse

def login(request):

    if request.method == 'GET':
        return render(request, 'armageddon_system/user/login.html')
    elif request.method == 'POST':
        logch = False

        if 'ID' in request.POST and 'pass' in request.POST:
            request.session['user_id'] = request.POST['ID']
            request.session['user_pass'] = request.POST['pass']
            logch = True

        if logch:
            print(request.session['user_id'])
            print(request.session['user_pass'])
            return render(request, 'armageddon_system/pay/log.html')
        else:
            return render(request, 'armageddon_system/user/login.html')

def logout(request):
    return render(request, 'armageddon_system/user/login.html')