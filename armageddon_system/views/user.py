from django.shortcuts import render
from armageddon_system.views import pay
from armageddon_system.models.dynamo_manager import DynamoManager as db


def login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'armageddon_system/user/login.html')

    elif request.method == 'POST':
        is_login_success = False
        dbm = db()

        if 'user_id' in request.POST and 'user_pass' in request.POST:
            user_id = request.POST['user_id']
            user_pass = request.POST['user_pass']

            if dbm.check_login_id(user_id, user_pass):
                request.session['user_id'] = user_id
                request.session['user_pass'] = user_pass
                is_login_success = True
                # session_saveメソッドを作る

            else:
                context['error'] = "IDまたはパスワードが違います"

        if is_login_success:
            return pay.log(request)

        else:
            return render(request, 'armageddon_system/user/login.html', context)


def logout(request):
    request.session.clear()
    return render(request, 'armageddon_system/user/login.html')
