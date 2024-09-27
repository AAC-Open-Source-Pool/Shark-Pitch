from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def Intrested_page(request):
    return render(request,'Interested_page.html')

def Startup_info(request):
    return render(request,'Startup_info.html')