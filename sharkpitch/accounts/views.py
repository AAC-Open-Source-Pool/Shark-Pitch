from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout as Logout,authenticate,login as Login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


#signUp

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        profession=request.POST['profession']
        location=request.POST['location']
        mobile=request.POST['mobile']
        user_type = request.POST.get('user_type')
        print(user_type)

        # Check if email already exists
        if Signin.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            # Hash the password before saving it
            #hashed_password = make_password(password)
            
            # Create a new user account
            #new_user = Signin(name=name, email=email, password=hashed_password)
            new_user = Signin(name=name, email=email, password=password, mobile=mobile, profession=profession, location=location,user_type=user_type)
            new_user.save()

            if user_type == "investor" or user_type == "user":
                messages.success(request, "Account created successfully!")
                return redirect('login')  # Redirect to Page 1 for Investor and User

            elif user_type == "startup":
                Login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Preliminary registration details saved!")
                return redirect('verification1')
            #messages.success(request, "Account created successfully!")
            #return redirect('accounts:login_view')  # Redirect to sign-in page after successful sign-up

    return render(request, 'sign_up_page.html')



# Login View
def login_view(request):
    print("gotin2")
    if request.method == "POST":
        print("gotin1")
        email = request.POST['email']
        password = request.POST['password']
        try:
            print(f"Attempting login with email: {email}, password: {password}")
            # Check if the user exists
            user = Signin.objects.get(email=email)
            print(f"User found: {user.email}")
            
            # Manually check if the password matches
            if user.password == password:  # Compare plain text passwords
                print("Password matches")
                # Set session variables
                Login(request, user)  # Log the user in
                print("User logged in successfully.")
                
                # Save or update login details (if you need to keep track of logins)
                login_record, created = login.objects.update_or_create(
                    email=user.email,
                    defaults={
                        'name': user.name,
                        'password': user.password,  # Save plain text as required
                    }
                )
                print("Login record saved or updated.")
                
                if created:
                    messages.success(request, "New login record created.")
                else:
                    messages.success(request, "Login record updated.")
                
                # Redirect to landing page
                messages.success(request, "Login successful.")
                return redirect('Investor_landing')
            else:
                messages.error(request, "Invalid password.")  # Handle incorrect password
        except Signin.DoesNotExist:
            messages.error(request, "User does not exist.")  # Handle non-existent user
        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, "An unexpected error occurred.")  # General error handling

    return render(request, 'login.html')
@login_required
def profile_view(request):
    print("gotin1")
    user = request.user._wrapped
    # Ensure user is authenticated
    if not request.user.is_authenticated:
        print("gotin2")
        return redirect('login')

    # Retrieve the user's data
    #user = Signin.objects.get(email=request.user.email)
    print("gotin3")
    # Render the appropriate template based on the user_type
    print(f"User type: {user.user_type}")
    print(f"User object: {user}")
    print(user.__dict__) 
    if user.user_type == 'investor':
        return render(request, 'Investor_profile.html', {'user': user})
    elif user.user_type == 'startup':
        try:
            # Fetch related data from the startup_register1 table
            startup_data = startup_register1.objects.filter(user=user).first()
            print(startup_data.SRNnumber)
        except startup_register1.DoesNotExist:
            print("No related startup data found.")

        # Pass both user and startup data to the template
        return render(request, 'Startup_info.html', {
            'user': user,
            'startup_data': startup_data,
        })
    else:
        return render(request, 'User_profile.html', {'user': user})
    print("gotin4")

@login_required
def Investor_landing(request):
    return render(request,'Investor_landing.html')

#startup description page view
def startup_description_view(request):
    print("Loading startup description page")

    # Ensure user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')

    # Get the currently logged-in user
    user = request.user._wrapped  # Assuming you're using a custom user model wrapped in `request.user`

    # Initialize all registration data as None
    startup_data = {
        'register1': None,
        'register2': None,
        'register3': None,
        'register4': None,
        'register5': None,
        'register6': None,
        'register7': None,
        'register8': None,
        'register9': None
    }

    # Fetch all related registration data for startup
    if user.user_type == 'startup':
        # Fetch the data from all 9 registration tables using .filter(user=user).first()
        startup_data['register1'] = startup_register1.objects.filter(user=user).first()
        startup_data['register2'] = startup_register2.objects.filter(user=user).first()
        startup_data['register3'] = startup_register3.objects.filter(user=user).first()
        startup_data['register4'] = startup_register4.objects.filter(user=user).first()
        startup_data['register5'] = startup_register5.objects.filter(user=user).first()
        startup_data['register6'] = startup_register6.objects.filter(user=user).first()
        startup_data['register7'] = startup_register7.objects.filter(user=user).first()
        startup_data['register8'] = startup_register8.objects.filter(user=user).first()
        startup_data['register9'] = startup_register9.objects.filter(user=user).first()

        # Pass the data to the template for rendering
        return render(request, 'Startup_description.html', {
            'user': user,
            'startup_data': startup_data,
        })

# Startup Registration Step 1

def startup_register1_view(request):
    print(request.user)
    if request.method == 'POST':
        SRNnumber = request.POST.get('SRNnumber')
        Doc = request.FILES.get('Doc')
        #print("gotin1")
        if request.user.is_authenticated and request.user.user_type == 'startup':
            if SRNnumber and Doc:
                startup_register1.objects.create(SRNnumber=SRNnumber, Doc=Doc,user=request.user)
                messages.success(request, 'Registration Step 1 completed.')
                #print("gotin2")
                return redirect('accounts:startup_register2_view')  # Redirect to the next registration step
            else:
                messages.error(request, 'Please fill out all fields.')
        return render(request, 'startup_verification_page1.html')

# Startup Registration Step 2
def startup_register2_view(request):
    print(request.user,request.user.user_type)
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')

        if request.user.is_authenticated and request.user.user_type == 'startup':
            if all([q1, q2, q3, q4, q5, q6, q7, q8]):
                startup_register2.objects.create(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8,user=request.user)
                messages.success(request, 'Registration Step 2 completed.')
                return redirect('accounts:startup_register3_view')  # Redirect to the next registration step
            else:
                messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page2.html')

# Startup Registration Step 3
def startup_register3_view(request):
    print(request.user,request.user.user_type)
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        if all([q1,q2,q3]):
            startup_register3.objects.create(q1=q1, q2=q2, q3=q3,user=request.user)
            messages.success(request, 'Registration Step 3 completed.')
            return redirect('accounts:startup_register4_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page3.html')


# Startup Registration Step 4
def startup_register4_view(request):
    print(request.user,request.user.user_type)
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register4.objects.create(q1=q1, q2=q2,user=request.user)
            messages.success(request, 'Registration Step 4 completed.')
            return redirect('accounts:startup_register5_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page4.html')


# Startup Registration Step 5
@login_required
def startup_register5_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register5.objects.create(q1=q1, q2=q2,user=request.user)
            messages.success(request, 'Registration Step 5 completed.')
            return redirect('accounts:startup_register6_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page5.html')


# Startup Registration Step 6
@login_required
def startup_register6_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register6.objects.create(q1=q1, q2=q2,user=request.user)
            messages.success(request, 'Registration Step 6 completed.')
            return redirect('accounts:startup_register7_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page6.html')
    

# Startup Registration Step 7
@login_required
def startup_register7_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        if all([q1,q2]):
            startup_register7.objects.create(q1=q1, q2=q2,user=request.user)
            messages.success(request, 'Registration Step 7 completed.')
            return redirect('accounts:startup_register8_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page7.html')

# Startup Registration Step 8
@login_required
def startup_register8_view(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        if all([q1,q2,q3]):
            startup_register8.objects.create(q1=q1, q2=q2, q3=q3,user=request.user)
            messages.success(request, 'Registration Step 8 completed.')
            return redirect('accounts:startup_register9_view')
        else:
            messages.error(request, 'Please fill out all fields.')
    return render(request, 'startup_verification_page8.html')

def startup_register9_view(request):
    return redirect('accounts:startup_register10_view')

 #Startup Registration Step 10
@login_required
def startup_register10_view(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        print("gotin2")
        if video:
            print("gotin1")
            startup_register10.objects.create(video=video,user=request.user)
            messages.success(request, 'Video uploaded successfully!')
            return redirect('Investor_landing') 
        else:
            messages.error(request, 'Please upload a video.')
    return render(request, 'startup_verification_page10.html')


#logout
def logout(request):
    Logout(request)  # Clear all session data
    messages.success(request, "Logged out successfully.")
    return redirect('login')