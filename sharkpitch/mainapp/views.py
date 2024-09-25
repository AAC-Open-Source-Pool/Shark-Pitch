from django.shortcuts import render

# Create your views here.

def Investor_landing(request):
    return render(request,'investor_landing.html')

def Investor_profile(request):
    return render(request,'investor_profile.html')

def User_profile(request):
    return render(request,'user_profile.html')