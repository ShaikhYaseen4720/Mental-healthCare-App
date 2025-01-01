from django.db import models
from django.contrib.auth.models import User

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    age = models.PositiveIntegerField()
    speciality = models.CharField(max_length=50, choices=[("Physician", "Physician"), ("Psychiatrist", "Psychiatrist")])
    is_doctor = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.speciality}"
    
class RepondToPatient(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses_as_doctor')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses_as_user')
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.doctor} => {self.user}"

