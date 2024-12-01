from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('investor_landing',views.Investor_landing,name='Investor_landing'),
    path('Investor_profile',views.Investor_profile,name='Investor_profile'),
    path('user_profile',views.User_profile,name='User_profile'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('verification1',views.verification1,name='verification1'),
    path('verification2',views.verification2,name='verification2'),
    path('verification3',views.verification3,name='verification3'),
    path('verification4',views.verification4,name='verification4'),
    path('verification5',views.verification5,name='verification5'),
    path('verification6',views.verification6,name='verification6'),
    path('verification7',views.verification7,name='verification7'),
    path('verification8/',views.verification8,name='verification8'),
    path('verification9',views.verification9,name='verification9'),
    path('verification10',views.verification10,name='verification10'),
    path('investor_description',views.investor_description,name='investor_description'),
    path('interested',views.interested,name='interested'),
    path('startup_info',views.startup_info,name='startup_info'),
    path('startup_home',views.startup_home,name='startup_home'),
    path('jitsi/<str:room_name>/', views.jitsi_room, name='jitsi_room'),
]
