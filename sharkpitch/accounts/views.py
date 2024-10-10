from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password

# Create your views here.

#signUp

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if email already exists
        if Signin.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            # Hash the password before saving it
            hashed_password = make_password(password)
            
            # Create a new user account
            new_user = Signin(name=name, email=email, password=hashed_password)
            new_user.save()

            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to sign-in page after successful sign-up

    return render(request, 'sign_up_page.html')



# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = login.objects.get(email=email, password=password)
            messages.success(request, 'Login successful!')
            return redirect('investor_landing')  

        except login.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')


# Startup Registration Step 1
def startup_register1_view(request):
    if request.method == 'POST':
        SRNnumber = request.POST.get('SRNnumber')
        Doc = request.FILES.get('Doc')
        if SRNnumber and Doc:
            startup_register1.objects.create(SRNnumber=SRNnumber, Doc=Doc)
            messages.success(request, 'Registration Step 1 completed.')
            return redirect('startup_register2')  # Redirect to the next registration step
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page1.html')

# Startup Registration Step 2
def startup_register2_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')
        
        if all([q1, q2, q3, q4, q5, q6, q7, q8]):
            startup_register2.objects.create(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8)
            messages.success(request, 'Registration Step 2 completed.')
            return redirect('startup_register3')  # Redirect to the next registration step
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page2.html')

# Startup Registration Step 3
def startup_register3_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
    if all([q1,q2,q3]):
        startup_register3_view.objects.create(q1=q1, q2=q2,q3=q3)
        messages.success(request, 'Registration Step 3 completed.')
        return redirect('startup_register4')
    else:
        messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page3.html')


# Startup Registration Step 4
def startup_register4_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
    if all([q1,q2]):
        startup_register3_view.objects.create(q1=q1, q2=q2)
        messages.success(request, 'Registration Step 4 completed.')
        return redirect('startup_register5')
    else:
        messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page4.html')


# Startup Registration Step 5
def startup_register5_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
    if all([q1,q2]):
        startup_register3_view.objects.create(q1=q1, q2=q2)
        messages.success(request, 'Registration Step 5 completed.')
        return redirect('startup_register6')
    else:
        messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page5.html')


# Startup Registration Step 6
def startup_register6_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
    if all([q1,q2]):
        startup_register3_view.objects.create(q1=q1, q2=q2)
        messages.success(request, 'Registration Step 6 completed.')
        return redirect('startup_register7')
    else:
        messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page6.html')
    

# Startup Registration Step 7
def startup_register7_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
    if all([q1,q2]):
        startup_register3_view.objects.create(q1=q1, q2=q2)
        messages.success(request, 'Registration Step 7 completed.')
        return redirect('startup_register8')
    else:
        messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page7.html')

# Startup Registration Step 8
def startup_register8_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
    if all([q1,q2,q3]):
        startup_register3_view.objects.create(q1=q1, q2=q2, q3=q3)
        messages.success(request, 'Registration Step 8 completed.')
        return redirect('startup_register9')
    else:
        messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page8.html')

def startup_register9_view(request):
    return redirect('startup_register10')

 #Startup Registration Step 10
def startup_register10_view(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        if video:
            startup_register10.objects.create(video=video)
            messages.success(request, 'Video uploaded successfully!')
            return redirect('investor_landing') 
        else:
            messages.error(request, 'Please upload a video.')
    return render(request, 'startup_register10.html')


#logout
def logout(request):
    auth.logout(request)
    return redirect("/")