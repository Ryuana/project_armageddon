from django.shortcuts import render
from django.http import HttpResponse

def linebot_qa_list(request):
    return render(request, 'armageddon_system/linebot/qa/list.html')