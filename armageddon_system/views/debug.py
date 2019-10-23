from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.models.model import FormsModel
import json
import random


def dynamo(request):
    if not FormsModel.exists():
        FormsModel.create_table(wait=True)
        rt = "テーブルを作成しました\n"
    else:
        rt = "テーブルを作成しませんでした<br>"
    id = str(FormsModel.count() + 1)
    form = FormsModel(random.randint(1,300))
    count = FormsModel.count()
    form.Form = {"FormName": "2ndTest",
                 "Fee":random.randint(1,300),
                 "IssuanceDays": 3,
                 "QR": "qrcode"
                 }
    rt = form.save()
    try:
        # fm = FormsModel.get(hash_key="9999")
        # form = json.dumps(dict(fm))
        # rt = fm.mapAttribute
        # rt= rt['testB']
        # d = {"aaa":123}
        form_list = []
        # for fm in FormsModel.scan():
        #     formId = fm.FormId
        #     test = fm.testClumn
        #     testL = fm.listAttribute
        #     m = {
        #         "FormID": formId,
        #         "test": test,
        #         "testL": testL,
        #         "testM": {
        #             "testA": fm.mapAttribute['testA'],
        #             "testB": fm.mapAttribute['testB'],
        #         }
        #     }
        #
        #     form_list.append(m)
            # rt += json.dumps(dict(fm))
            # try:
            #     rt += fm.listAttribute
            # except:
            #     rt += "None"
            # rt += "<br>"
        rt = form_list
    except Exception as e:
        rt = e
    return HttpResponse(rt)
