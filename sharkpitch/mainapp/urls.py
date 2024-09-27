from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('home',views.home,name='home'),
    path('investor_landing',views.Investor_landing,name='Investor_landing'),
    path('Investor_profile',views.Investor_profile,name='Investor_profile'),
    path('User_profile',views.User_profile,name='User_profile'),
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('verification1',views.verification1,name='verification1'),
    path('verification2',views.verification2,name='verification2'),
    path('verification3',views.verification3,name='verification3'),
    path('verification4',views.verification4,name='verification4'),
    path('verification5',views.verification5,name='verification5'),
    path('verification6',views.verification6,name='verification6'),
    path('verification7',views.verification7,name='verification7'),
    path('verification8',views.verification8,name='verification8'),
    path('verification9',views.verification9,name='verification9'),
    path('verification10',views.verification10,name='verification10'),
]
