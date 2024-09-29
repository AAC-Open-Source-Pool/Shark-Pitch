from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def Startup_home(request):
    return render(request,'Startup_home.html')