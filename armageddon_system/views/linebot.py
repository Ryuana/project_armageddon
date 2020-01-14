from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.files.storage import  default_storage
import datetime
from armageddon_system.models.qa import QA
from armageddon_system.models.dynamo_manager import DynamoManager as db


# メッセージ一覧
def display_messages(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    all_message_list = dbm.get_message_list()
    message_list = []
    for i in reversed(range(len(all_message_list))):
        message = {}
        t_with_tz = all_message_list[i]['Message']['Timestamp']['S']
        t_str, tz = t_with_tz[:-5], t_with_tz[-5:]
        t = datetime.datetime.strptime(t_str, "%Y-%m-%dT%H:%M:%S.%f")
        message['message_id'] = (all_message_list[i]['MessageId'])
        message['timestamp'] = t.strftime("%Y-%m-%d")
        message['message_content'] = all_message_list[i]['Message']['MessageContent']['S']
        try:
            message['image_path'] = all_message_list[i]['Message']['ImagePath']['S']
        except Exception:
            message['image_path'] = ""
        message_list.append(message)
    message_list.sort(key=lambda x: x['message_id'])
    context['message'] = message_list
    return render(request, 'armageddon_system/linebot/msg/list.html', context)


# メッセージ編集画面
def edit_message(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    if 'message_id' in request.POST:
        context['message_id'] = request.POST['message_id']
        context['message'] = dbm.get_message(int(context['message_id']))
    else:
        context['message_id'] = dbm.get_next_message_id()
        context['message'] = {}
    return render(request, 'armageddon_system/linebot/msg/edit.html', context)


# メッセージ保存時
def save_message(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    context['message_id'] = request.POST['message_id']
    context['message'] = request.POST['message']
    if request.POST['message'] ==  ' ':
        context['message'] = " "
    if 'file' in request.FILES:
        context['image'] = str(request.FILES['file'])
        image = request.FILES['file']
        default_storage.save('armageddon_system/static/armageddon_system/' + str(request.FILES['file']), ContentFile(image.read()))
    else:
        context['image'] = None
    context['time_stamp'] = str(datetime.datetime.today()).split(" ")[0]
    dbm.save_message_list(context)

    return display_messages(request)

def delete_message(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    try:
        dbm.del_message_list(request.GET['message_id'])
    except KeyError:
        pass
    return HttpResponse("削除成功")


def display_qa_list(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    context['qa_list'] = dbm.get_qa_all()
    context['max_id'] = dbm.get_next_qa_id()

    return render(request, 'armageddon_system/linebot/qa/list.html', context)

def save_qa(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    try:
        context['qa_id'] = request.GET['qa_id']
        context['questions'] = request.GET['questions'].split(",")
        context['answer'] = request.GET['answer']
        dbm.save_qa(context)
    except KeyError:
        pass
    return HttpResponse("保存成功")


def delete_qa(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    try:
        dbm.del_qa(request.GET['qa_id'])
    except KeyError:
        pass
    return HttpResponse("削除成功")
