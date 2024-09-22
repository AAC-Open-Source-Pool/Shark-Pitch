from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('login', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),

    path('startup_verification_page1', views.startup_verification1, name='startup_verification1'),
    path('startup_verification_page2', views.startup_verification2, name='startup_verification2'),
    path('startup_verification_page3', views.startup_verification3, name='startup_verification3'),
    path('startup_verification_page4', views.startup_verification4, name='startup_verification4'),
    path('startup_verification_page5', views.startup_verification5, name='startup_verification5'),
    path('startup_verification_page6', views.startup_verification6, name='startup_verification6'),
    path('startup_verification_page7', views.startup_verification7, name='startup_verification7'),
    path('startup_verification_page8', views.startup_verification8, name='startup_verification8'),
    path('startup_verification_page9', views.startup_verification9, name='startup_verification9'),
    path('startup_verification_page10', views.startup_verification10, name='startup_verification10'),

    path('investor_description', views.investor_description, name='investor_description'),
]
