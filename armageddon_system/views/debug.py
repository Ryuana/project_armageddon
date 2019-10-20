from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.models.form_model import FormsModel
import json
import random

def dynamo(request):
    rt = "aaa"
    if not FormsModel.exists():
        FormsModel.create_table(wait=True)
        rt = "テーブルを作成しました"
    else:
        rt = "テーブルを作成しませんでした"
    # id = str(FormsModel.count() + 1)
    # form = FormsModel(random.randint(1,300))
    # count = FormsModel.count()
    # form.Form = {"FormName": "2ndTest",
    #              "Fee":random.randint(1,300),
    #              "IssuanceDays": 3,
    #              "QR": "qrcode"
    #              }
    # form.save()
    form = FormsModel()
    rt = form.scan()
    return HttpResponse([rt])
