from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.dynamo_models import dynamodb_model

def index(request):
    db = dynamodb_model.dynamo.get("armageddon")


    return render(request, 'armageddon_system/index.html',{'msg':db})