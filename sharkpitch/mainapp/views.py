from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign_up_page.html')

def startup_verification(request):
    return render(request, 'startup_verification_page.html')

def investor_description(request):
    return render(request, 'investor_description_page.html')
