from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from .models import Profile, MentalHealthAssessment
from django.contrib import messages
from django.urls import reverse
from doctors.models import RepondToPatient

# Create your views here.
def index(request):
    return render(request, "index.html")

def loginUser(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username = username).exists()
        if not user:
            messages.error(request, "username not found")
            return redirect(reverse("login"))

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfull")
            return redirect("/dashboard/")
        
        else:
            messages.error(request, "password is incorrect")
            return redirect(reverse("login"))

        
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        dob = data.get("dob")
        sex = data.get("sex")
        mental_status = data.get("mental_status")
        height = data.get("height")
        weight = data.get("weight")
        contact_number = data.get("contact_number")
        email = data.get("email")
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        username = first_name +" "+ last_name

        isUser = User.objects.filter(username = username)
        if isUser.exists():
            messages.error(request, "User already exists")
            return redirect("/register/")

        if password != password_confirmation:
            messages.error(request, "User already exists")
            return redirect("/register/")
            
        user = User(username = username)
        user.set_password(password)
        user.save()
        
        Profile.objects.create(user = user, fname = first_name, lname = last_name, dob = dob, sex = sex, mental_status = mental_status,email = email, height = height, weight = weight, number = contact_number, password = password)
        messages.success(request, "Registration done successfully")
        return redirect("/")
        
    return render(request, 'register.html')

def dashboard(request):

    return render(request, "dashboard.html")

@login_required
def submit_assessment(request):
    if request.method == 'POST':
        # Create a new assessment entry and save the data from the form
        assessment = MentalHealthAssessment(
            user=request.user,
            question1=request.POST.get('question1'),
            question2=request.POST.get('question2'),
            question3=request.POST.get('question3'),
            question4=request.POST.get('question4'),
            question5=request.POST.get('q5'),
            question6=request.POST.get('q6'),
            question7=request.POST.get('q7'),
            question8=request.POST.get('q8'),
            question9=request.POST.get('q9'),
            question10=request.POST.get('q10'),
            question11=request.POST.get('q11'),
            question12=request.POST.get('q12'),
            question13=request.POST.get('q13'),
            question14=request.POST.get('q14')
        )
        assessment.save()
        messages.success(request, "data saved successfully. Thankyou for putting your trust in our app")
        return redirect('/dashboard/') 
    
@login_required
def responseFromDoctor(request):
    responses = RepondToPatient.objects.filter(user = request.user)
    return render(request, "response.html", {"responses" : responses})

def logoutUser(request):
    logout(request)
    return redirect(reverse("login"))

