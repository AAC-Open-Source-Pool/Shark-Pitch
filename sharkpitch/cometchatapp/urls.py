from django.urls import path
from .views import cometchat_view

urlpatterns = [
       path('index/', cometchat_view, name='cometchat'),
   ]
