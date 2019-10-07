from django.shortcuts import render
from django.http import HttpResponse
from armageddon_system.dynamo_models import dynamodb_model

def index(request):
    db = dynamodb_model.dynamo.get(hash_key="armageddon",range_key="1")


    return render(request, 'armageddon_system/index.html',{'msg':db.attribute_values})