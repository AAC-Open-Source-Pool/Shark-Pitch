from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout as Logout,authenticate,login as Login
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
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
                Login(request, user,backend='django.contrib.auth.backends.ModelBackend')  # Log the user in
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
                #return redirect('accounts:Investor_landing')
                if(user.user_type=='startup'):
                    return redirect('accounts:startup_landing')
                else:
                    return redirect('accounts:Investor_landing')
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
    print("hey1")
    videos = startup_register10.objects.all()
    video_data = []

    for video in videos:
        print("hey2")
        try:
            # Get founder data (single query for Founder_Name and Company_Name)
            founder_data = startup_register1.objects.filter(user=video.user).first()
            if founder_data:
                print("entered")
                Founder_Name = founder_data.Founder_Name
                Company_Name = founder_data.Company_Name
            else:
                Founder_Name = "Unknown"
                Company_Name = "Unknown"
            # Get tag data
            tag_data = startup_register5.objects.filter(user=video.user).first()
            tag = tag_data.q2 if tag_data else "other"

        except Exception as e:
            print(f"Error fetching data for user {video.user}: {e}")
            Founder_Name = "Unknown"
            Company_Name = "Unknown"
            tag = "other"
        # Append video data
        video_data.append({
            'video_url': video.video.url,
            'Founder_Name': founder_data.Founder_Name,
            'Company_Name': founder_data.Company_Name,
            'user_id':founder_data.user_id,
            'tag': tag
        })
        print(video_data)

    # Render the page with video data
    return render(request, 'Investor_landing.html', {'video_data': video_data})

#startup description page view
def startup_home_view(request,user_id):
    print("Loading startup description page")

    # Ensure user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')
    startup = get_object_or_404(startup_register1, user_id=user_id)
    info1 = Signin.objects.filter(id=user_id).first()
    info10 = startup_register10.objects.filter(user=startup.user).first()
    info8 = startup_register8.objects.filter(user=startup.user).first()
    info7 = startup_register7.objects.filter(user=startup.user).first()
    info6 = startup_register6.objects.filter(user=startup.user).first()
    info5 = startup_register5.objects.filter(user=startup.user).first()
    info4 = startup_register4.objects.filter(user=startup.user).first()
    info3 = startup_register3.objects.filter(user=startup.user).first()
    info2 = startup_register2.objects.filter(user=startup.user).first()
    # Consolidate all the details into a dictionary
    details = {
        'Founder_Name': startup.Founder_Name,
        'Company_Name': startup.Company_Name,
        'q1':info3.q1,
        'q2':info4.q1,
        'q3':info6.q2,
        'q4':info6.q1,
        'q5':info8.q1,
        'mail':info1.email,
        #'Video_URL': info10.video.url if info10 else None,
        'Video_URL':'media/media/videos/pitch5.mp4',
        # Add other fields as needed
    }
    print(details)
    return render(request, 'Startup_home.html', {'details': details})
    

def startup_landing(request):
    print("Loading startup description page")
    user = request.user
    print(user)
    # Ensure user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')
    startup = startup_register1.objects.filter(user=user).first()
    info10 = startup_register10.objects.filter(user=user).first()
    info8 = startup_register8.objects.filter(user=user).first()
    info7 = startup_register7.objects.filter(user=user).first()
    info6 = startup_register6.objects.filter(user=user).first()
    info5 = startup_register5.objects.filter(user=user).first()
    info4 = startup_register4.objects.filter(user=user).first()
    info3 = startup_register3.objects.filter(user=user).first()
    info2 = startup_register2.objects.filter(user=user).first()
    # Consolidate all the details into a dictionary
    details = {
        'Founder_Name': startup.Founder_Name,
        'Company_Name': startup.Company_Name,
        'q1':info3.q1,
        'q2':info4.q1,
        'q3':info6.q2,
        'q4':info6.q1,
        'q5':info8.q1,
        'mail':user.email,
        #'Video_URL': info10.video.url if info10 else None,
        'Video_URL':'media/media/videos/pitch5.mp4',
        # Add other fields as needed
    }
    print(details)
    return render(request, 'Startup_home.html', {'details': details})
    

# Startup Registration Step 1

def startup_register1_view(request):
    print(request.user)
    if request.method == 'POST':
        SRNnumber = request.POST.get('SRNnumber')
        Doc = request.FILES.get('Doc')
        Company_Name=request.POST.get('companyName')
        Founder_Name=request.POST.get('founderName')
        print(Company_Name)
        print(Founder_Name)
        if request.user.is_authenticated and request.user.user_type == 'startup':
            print("gotin3")
            if SRNnumber and Doc:
                print('got in 4')
                startup_register1.objects.create(SRNnumber=SRNnumber, Doc=Doc,Company_Name=Company_Name,Founder_Name=Founder_Name,user=request.user)
                messages.success(request, 'Registration Step 1 completed.')
                print("gotin2")
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
            return redirect('accounts:Investor_landing') 
        else:
            messages.error(request, 'Please upload a video.')
    return render(request, 'startup_verification_page10.html')


#logout
def logout(request):
    Logout(request)  # Clear all session data
    messages.success(request, "Logged out successfully.")
    return redirect('login')