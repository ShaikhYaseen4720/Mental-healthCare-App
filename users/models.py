from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    dob = models.DateTimeField()
    sex = models.CharField(max_length=10)
    mental_status = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.fname + " " + self.lname
    
class MentalHealthAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=50)
    question3 = models.CharField(max_length=50)
    question4 = models.CharField(max_length=50)
    question5 = models.CharField(max_length=50)
    question6 = models.CharField(max_length=50)
    question7 = models.CharField(max_length=50)
    question8 = models.CharField(max_length=50)
    question9 = models.CharField(max_length=50)
    question10 = models.CharField(max_length=50)
    question11 = models.CharField(max_length=50)
    question12 = models.CharField(max_length=50)
    question13 = models.CharField(max_length=50)
    question14 = models.CharField(max_length=50)
    def __str__(self):
        return f"Assessment by {self.user.username}"