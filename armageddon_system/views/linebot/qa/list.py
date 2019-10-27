from django.shortcuts import render
from armageddon_system.models.qa import QA
from armageddon_system.models.DynamoManager import DynamoManager as db
from django.http import HttpResponse

def display_qa_list(request):

    qa_list: list[QA] = db.get_pay_item_all()

    return render(request, 'armageddon_system/linebot/qa/list.html', {'qa_list': qa_list})

def qa_save(request,qa_list:QA):

    """
    追加した列の値を受け取り、dynamoDBに保存する処理
    """

    return HttpResponse()

def qa_delete(request,qa_id):

    """
    qa_idをもとに該当するデータを削除する処理
    """
    return HttpResponse