from django.shortcuts import render

# Create your views here.

def Investor_landing(request):
    return render(request,'investor_landing.html')
def Investor_profile(request):
    return render(request,'investor_profile.html')
def User_profile(request):
    return render(request,'user_profile.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'sign_up_page.html')
def verification1(request):
    return render(request,'startup_verification_page1.html')
def verification2(request):
    return render(request,'startup_verification_page2.html')
def verification3(request):
    return render(request,'startup_verification_page3.html')
def verification4(request):
    return render(request,'startup_verification_page4.html')
def verification5(request):
    return render(request,'startup_verification_page5.html')
def verification6(request):
    return render(request,'startup_verification_page6.html')
def verification7(request):
    return render(request,'startup_verification_page7.html')
def verification8(request):
    return render(request,'startup_verification_page8.html')
def verification9(request):
    return render(request,'startup_verification_page9.html')
def verification10(request):
    return render(request,'startup_verification_page10.html')