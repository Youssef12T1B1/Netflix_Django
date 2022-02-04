from urllib import request
from django.shortcuts import render



def home(request):
    return render(request , 'index.html')

def login(request):
    return render(request , 'login_register/login.html')

def register(request):
    return render(request , 'login_register/signup.html')







