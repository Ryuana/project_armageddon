from django.shortcuts import render
from django.http import HttpResponse


def msg_list(request):
    return render(request, 'armageddon_system/linebot/msg/list.html')

def msg_edit(request):
    return render(request, 'armageddon_system/linebot/msg/edit.html')

def qa_list(request):
    return render(request, 'armageddon_system/linebot/qa/list.html')