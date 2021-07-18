from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("loginUser",views.loginUser,name='loginUser'),
    path("logoutUser",views.logoutUser,name='logoutUser'),
    path("signupUser",views.signupUser,name='signupUser')
   
]