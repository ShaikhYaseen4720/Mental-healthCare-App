from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import DoctorProfile, RepondToPatient
from django.contrib.auth import authenticate, login, logout
from users.models import MentalHealthAssessment
from django.contrib.auth.decorators import login_required

def doctorLogin(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)
        if not user.exists:
            messages.error(request, "username not found")
            return redirect(reverse("doctorLogin"))
        
        user = DoctorProfile.objects.filter(user = user[0]).exists()
        if not user:
            messages.error(request, "username not found")
            return redirect(reverse("doctorLogin"))


        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect(reverse("doctorDashboard"))  
        else:
            messages.error(request, "Invalid email or password.")
        return redirect(reverse("doctorLogin"))

    return render(request, "doctor/doctorLogin.html")

def doctorRegister(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        speciality = request.POST.get("speciality")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect(reverse("doctorRegistration"))

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect(reverse("doctorRegistration"))


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        doctor_profile = DoctorProfile(
            user=user,
            gender=gender,
            age=age,
            speciality=speciality,
        )
        doctor_profile.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect(reverse("doctorLogin"))

    return render(request, "doctor/registration.html")

@login_required
def dashboard(request):
    users = MentalHealthAssessment.objects.all()
    # print(users)
    return render(request, "doctor/dashboard.html", {'users': users})

@login_required
def patient_response(request, id):
    user = MentalHealthAssessment.objects.get(id = id)
    return render(request, "doctor/user-response.html", {"user" : user})

@login_required
def respondFromDoctor(request, id):
    user = User.objects.get(id = id)
    message = request.POST.get("message")
    RepondToPatient.objects.create(user = user, doctor = request.user, message = message)
    return redirect(reverse("doctorDashboard"))

@login_required
def logoutUser(request):
    print(request.user)
    logout(request)
    return redirect(reverse("doctorLogin"))


@login_required
def deleteResponse(request, id):
    MentalHealthAssessment.objects.get(id = id).delete()
    return redirect(reverse("doctorDashboard"))