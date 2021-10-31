from django.shortcuts import redirect, render
from .models import studentInfo, userInfo
from .forms import Userform,UserInfoform,StudentInfoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_user(request):
    userform=Userform()
    userInfoform=UserInfoform()

    if request.method=='POST':
        userform=Userform(request.POST)
        userInfoform=UserInfoform(request.POST)
        
        if userform.is_valid() and userInfoform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            user_info = userInfoform.save(commit=False)
            user_info.user = user
            user_info.save()
            return render(request,"index.html")

        else:
            context = {
                'user_form.errors': userform.errors, 'user_info_form.errors': userInfoform.errors,
                'user_form': userform, 'user_info_form': userInfoform
            }
            return render(request, 'signup_user.html', context)

    contaxt={"userform":userform,"userInfoform":userInfoform}

    return render(request,'signup_user.html',contaxt)

def signup_student(request):
    studentInfoform=StudentInfoForm()

    if request.method=='POST':
        studentInfoform=StudentInfoForm(request.POST)

        if studentInfoform.is_valid():

            user_info = studentInfoform.save(commit=False)
            user_info.save()
            return render(request,'index.html')
        else:
            context = {
                'user_info_form.errors': studentInfoform.errors,
                'user_info_form': studentInfoform
            }
            return render(request, 'signup_student.html', context)


    contaxt={"studentInfoform":studentInfoform}
    return render(request,'signup_student.html',contaxt)

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def after_login(request):
    return render(request,'after_login.html')

@login_required(login_url="login")
def user_table(request):
    data=userInfo.objects.all()
    context={"data":data}
    return render(request,'user_table.html',context)

@login_required(login_url="login")
def student_table(request):
    data=studentInfo.objects.all()
    context={"data":data}
    return render(request,'student_table.html',context)

def admin(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=='admin' and password=='password':
             return render(request,'after_login.html')
    return render(request,'admin_login.html')