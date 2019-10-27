from django.shortcuts import render
from armageddon_system.models.message import Message
from armageddon_system.models.DynamoManager import DynamoManager as db

def edit_message(request):

    return render(request, 'armageddon_system/linebot/msg/edit.html')


#TODO:仕様に変更あり
def save_message(request,message,img):

    """
    dynamoDBからIDをもらう
    #Messageのインスタンス化(ID,message,img)&messages配列にappend
    """

    return render(request, 'armageddon_system/linebot/msg/list.html')


#TODO:仕様に変更あり
def send_message(request, message_id):

    """
    message_idをもとに該当するデータを送信する処理
    """

    return render(request, 'armageddon_system/linebot/msg/list.html')