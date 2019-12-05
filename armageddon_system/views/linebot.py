from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
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
    message_list.sort(key=lambda x:x['message_id'])
    context['message'] = message_list
    return render(request, 'armageddon_system/linebot/msg/list.html', context)


# メッセージ編集画面
def edit_message(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    context['message_id'] = request.POST['message_id']
    # message_idを元にmessage取り出す
    dbm = db()
    context['message'] = dbm.get_message(int(context['message_id']))
    # context渡す
    return render(request, 'armageddon_system/linebot/msg/edit.html',context)


# メッセージ保存時
def save_message(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    message = request.GET['message']
    img = request.GET['img']
    dbm.save_message_list(message, img)

    return render(request, 'armageddon_system/linebot/msg/list.html')


def display_qa_list(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    context['qa_list'] = dbm.get_qa_all()

    return render(request, 'armageddon_system/linebot/qa/list.html', context)


def save_qa(request):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    # qa_idの最新の値を取り出す処理
    questions = str(request.GET['questions']).split(",")
    answer = request.answer
    # dbm.save_qa(qa_id,questions,answer)


def delete_qa(request, qa_id):
    context = {}
    if 'user_id' not in request.session:
        context['error'] = "ログインしてください"
        return render(request, 'armageddon_system/user/login.html', context)
    dbm = db()
    dbm.del_qa(qa_id)
