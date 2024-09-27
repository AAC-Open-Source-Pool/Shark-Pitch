from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('home',views.home,name='home'),
    path('Interested_page',views.Intrested_page,name='intrested_page'),
    path('',views.Startup_info,name='startup_info'),
]
