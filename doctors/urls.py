from django.urls import path
from doctors.views import *

urlpatterns = [
    path("", doctorLogin, name="doctorLogin"),
    path("registration", doctorRegister, name="doctorRegistration"),
    path("dashboard", dashboard, name="doctorDashboard"),
    path("respond/<id>", patient_response, name="respond"),
    path("response-to-user/<id>", respondFromDoctor, name="respond-from-doctor"),
    path("logout/", logoutUser, name="logoutUser"),
    path("delete/<id>", deleteResponse, name="deleteResponse")
]