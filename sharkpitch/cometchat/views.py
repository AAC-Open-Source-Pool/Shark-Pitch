from django.shortcuts import render
from django.http import JsonResponse

def register_user_view(request):
    if request.method == 'POST':
        cometchat_uid = request.POST.get('uid')
        name = request.POST.get('name')
        response = register_user(cometchat_uid, name)
        return JsonResponse(response)
import requests

def register_user(cometchat_uid, name):
    url = "https://api-{IN}.cometchat.io/v3/users"
    headers = {
        "Content-Type": "application/json",
        "appId": "267727497461a0e1",
        "apiKey": "0ac2aea0a9c16bcded63bb07ab7428dfeb3ca661"
    }
    data = {
        "uid": cometchat_uid,
        "name": name
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
