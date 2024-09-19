from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.login, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('startup-verification/', views.startup_verification, name='startup_verification'),
    path('investor-description/', views.investor_description, name='investor_description'),
]
