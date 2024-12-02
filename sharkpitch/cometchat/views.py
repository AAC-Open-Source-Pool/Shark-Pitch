from django.http import JsonResponse
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from django.conf import settings
from django.shortcuts import render
from twilio.rest import Client

def create_conversation(request):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    conversation = client.conversations.conversations.create(
        friendly_name='New Chat Room'
    )
    return JsonResponse({'sid': conversation.sid, 'friendly_name': conversation.friendly_name})

def generate_token(request):
    identity = request.GET.get('identity', 'AnonymousUser')

    # Create a Twilio Access Token
    token = AccessToken(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN,
        settings.TWILIO_CHAT_SERVICE_SID,
    )
    token.identity = identity

    # Grant access to Chat
    chat_grant = ChatGrant(service_sid=settings.TWILIO_CHAT_SERVICE_SID)
    token.add_grant(chat_grant)

    return JsonResponse({'token': token.to_jwt().decode('utf-8')})


def chat_home(request):
    return render(request, 'chat.html')

def chat(request):
    return render(request, 'cometchat/chat.html')  # Target template