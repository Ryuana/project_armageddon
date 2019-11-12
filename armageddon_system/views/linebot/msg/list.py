from django.shortcuts import render
from armageddon_system.models.message import Message
from armageddon_system.models.dynamo_manager import DynamoManager as db
from django.http import HttpResponse

def display_message_item(request):

    messages: list[Message] = db.get_message_list

    return render(request, 'armageddon_system/pay/item/list.html', {'messages': messages})

def delete_message_item(request, message_id):

    """
    message_idをもとに該当するデータを削除する処理
    """
    return HttpResponse()