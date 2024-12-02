from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('get_token/', views.generate_token, name='get_token'),
    path('chat/', views.chat_home, name='chat'),# Target page
]

app_name="cometchat"