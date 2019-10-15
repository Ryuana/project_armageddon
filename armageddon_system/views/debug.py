from django.shortcuts import render
from django.http import HttpResponse

def dynamo(request):
    rt = "aaa"

    return HttpResponse(rt)