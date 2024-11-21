from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


#signUp

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST.get('user_type')

        # Check if email already exists
        if Signin.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            # Hash the password before saving it
            #hashed_password = make_password(password)
            
            # Create a new user account
            #new_user = Signin(name=name, email=email, password=hashed_password)
            new_user = Signin(name=name, email=email, password=password)
            new_user.save()

            if user_type == "investor" or user_type == "user":
                messages.success(request, "Account created successfully!")
                return redirect('login')  # Redirect to Page 1 for Investor and User

            elif user_type == "startup":
                messages.success(request, "Preliminary registration details saved!")
                return redirect('verification1')
            #messages.success(request, "Account created successfully!")
            #return redirect('accounts:login_view')  # Redirect to sign-in page after successful sign-up

    return render(request, 'sign_up_page.html')



# Login View
def login_view(request):
    if request.method == "POST":
        #print("gotin")
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Signin.objects.get(email=email)
            #print(f"User password from DB: {user.password}")  # Hashed password in DB
            #print(f"Entered password: {password}")  # Password entered by user
            #if check_password(password, user.password):
            if password == user.password:
                request.session['user_id'] = user.id 
                request.session['user_name'] = user.name
                messages.success(request, "Login successful.")
                login_record = login(name=user.name, email=user.email, password=user.password)
                login_record.save()
                return redirect('Investor_landing')
            else:
                messages.error(request, "Invalid password.")
        except Signin.DoesNotExist:
            messages.error(request, "User does not exist.")
    return render(request, 'login.html')

def Investor_landing(request):
    return render(request,'Investor_landing.html')

# Startup Registration Step 1
def startup_register1_view(request):
    if request.method == 'POST':
        SRNnumber = request.POST.get('SRNnumber')
        Doc = request.FILES.get('Doc')
        #print("gotin1")
        if SRNnumber and Doc:
            startup_register1.objects.create(SRNnumber=SRNnumber, Doc=Doc)
            messages.success(request, 'Registration Step 1 completed.')
            #print("gotin2")
            return redirect('accounts:startup_register2_view')  # Redirect to the next registration step
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
            return redirect('accounts:startup_register3_view')  # Redirect to the next registration step
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
            startup_register3.objects.create(q1=q1, q2=q2, q3=q3)
            messages.success(request, 'Registration Step 3 completed.')
            return redirect('accounts:startup_register4_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page3.html')


# Startup Registration Step 4
def startup_register4_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register4.objects.create(q1=q1, q2=q2)
            messages.success(request, 'Registration Step 4 completed.')
            return redirect('accounts:startup_register5_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page4.html')


# Startup Registration Step 5
def startup_register5_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register5.objects.create(q1=q1, q2=q2)
            messages.success(request, 'Registration Step 5 completed.')
            return redirect('accounts:startup_register6_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page5.html')


# Startup Registration Step 6
def startup_register6_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register6.objects.create(q1=q1, q2=q2)
            messages.success(request, 'Registration Step 6 completed.')
            return redirect('accounts:startup_register7_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page6.html')
    

# Startup Registration Step 7
def startup_register7_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register7.objects.create(q1=q1, q2=q2)
            messages.success(request, 'Registration Step 7 completed.')
            return redirect('accounts:startup_register8_view')
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
            startup_register8.objects.create(q1=q1, q2=q2, q3=q3)
            messages.success(request, 'Registration Step 8 completed.')
            return redirect('accounts:startup_register9_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page8.html')

def startup_register9_view(request):
    return redirect('accounts:startup_register10_view')

 #Startup Registration Step 10
def startup_register10_view(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        print("gotin2")
        if video:
            print("gotin1")
            startup_register10.objects.create(video=video)
            messages.success(request, 'Video uploaded successfully!')
            return redirect('Investor_landing') 
        else:
            messages.error(request, 'Please upload a video.')
    return render(request, 'startup_verification_page10.html')


#logout
def logout(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "Logged out successfully.")
    return redirect('login')