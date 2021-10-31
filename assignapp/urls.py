from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminpanel/',views.admin,name='admin'),
    path('after_login/',views.after_login,name='after_login'),
    path('user_table/',views.user_table,name='user_table'),    
    path('student_table/',views.student_table,name='student_table'),    
    path('signup_user/', views.signup_user, name='signup_user'),
    path('signup_student/', views.signup_student, name='signup_student'),
    path('login/', views.login, name='login'),
]