from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
]

class userInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userstatus=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class studentInfo(models.Model):
    Internship_choice=[
        ("FE","Front-end web developer"),
        ("BE","Back-end web developer")
    ]
    studentname=models.CharField(max_length=50)
    Collegename=models.CharField(max_length=50)
    Specialization=models.CharField(max_length=50)
    Degreename=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    Internship=models.CharField(max_length=50,choices=Internship_choice)
    PhoneNumber=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    Notes=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.studentname