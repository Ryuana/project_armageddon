from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.models.dynamo_manager import DynamoManager as db

def display_messages(request):
    dbm = db()
    messages = dbm.get_message_list()
    return render(request, 'armageddon_system/linebot/msg/list.html', {'messages': messages})
def msg_edit(request):
    return render(request, 'armageddon_system/linebot/msg/edit.html')

def qa_list(request):
    return render(request, 'armageddon_system/linebot/qa/list.html')