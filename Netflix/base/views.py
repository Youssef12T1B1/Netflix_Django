from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def home(request):
    return render(request , 'index.html')


method_decorator(login_required)
def profile(request):
    profiles = request.user.profiles.all()
    return render(request,'profileList.html' , {
        'profiles' : profiles
    })






