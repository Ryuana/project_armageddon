from django.shortcuts import render
from armageddon_system.models.form import Form
from armageddon_system.models.DynamoManager import DynamoManager as db
from django.http import HttpResponse

def display_form_item(request):

    forms: list[Form] = db.get_pay_item_all()

    return render(request, 'armageddon_system/pay/item/list.html', {'forms': forms})

def save_form_item(request,forms):

    """
    追加した列の値を受け取り、dynamoDBに保存する処理
    """

    return HttpResponse()

def delete_form_item(request, form_id):

    """
    form_idをもとに該当するデータを削除する処理
    """
    return HttpResponse()