from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model

from .models import userInfo,studentInfo

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','password']

class UserInfoform(forms.ModelForm):
    class Meta():
        model=userInfo
        fields=['userstatus']

class StudentInfoForm(forms.ModelForm):
    class Meta():
        model=studentInfo
        fields=['studentname','Collegename','Specialization','Degreename','email','Internship','PhoneNumber','Location','Gender','Notes']