from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from armageddon_system.models.qa import QA
from armageddon_system.models.dynamo_manager import DynamoManager as db

#メッセージ一覧
def display_messages(request):

    dbm = db()
    context = {}
    context['message'] = dbm.get_message_list()
    return render(request, 'armageddon_system/linebot/msg/list.html', context)

#メッセージ編集画面
def edit_message(request, message_id):

    #message_idを元にmessage取り出す
    context = {}
    #context['message'] = get_message

    #context渡す
    return render(request, 'armageddon_system/linebot/msg/edit.html')

#メッセージ保存時
def save_message(request):

    dbm = db()
    message = request.GET['message']
    img = request.GET['img']
    dbm.save_message_list(message, img)

    return render(request, 'armageddon_system/linebot/msg/list.html')

def display_qa_list(request):

    dbm = db()
    context = {}
    context['qa_list'] = dbm.get_qa_all()

    return render(request, 'armageddon_system/linebot/qa/list.html', context)

def save_qa(request):

    dbm = db()
    #qa_idの最新の値を取り出す処理
    questions = str(request.GET['questions']).split(",")
    answer = request.answer
    #dbm.save_qa(qa_id,questions,answer)

def delete_qa(request, qa_id):

    dbm = db()
    dbm.del_qa(qa_id)