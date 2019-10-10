from django.shortcuts import render
from django.http import HttpResponse

def linebot_msg_edit(request):
    return render(request, 'armageddon_system/linebot/msg/edit.html')