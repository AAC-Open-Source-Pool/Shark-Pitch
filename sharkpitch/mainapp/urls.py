from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('investor_landing',views.Investor_landing,name='Investor_landing'),
    path('Investor_profile',views.Investor_profile,name='Investor_profile'),
    path('',views.User_profile,name='User_profile'),
]
