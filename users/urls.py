from django.urls import path
from .views import *

urlpatterns = [
   path("", index, name="app"),
   path("login/", loginUser, name = "login"),
   path("register/", register, name="register"),
   path("dashboard/", dashboard, name="dashboard"),
   path('submit_assessment/', submit_assessment, name='submit_assessment'),
   path('responses',responseFromDoctor , name="respond_from_doctor"),
   path("logoutUserAccount", logoutUser, name="logoutUserAccount")
]
