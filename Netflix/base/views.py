from urllib import request
from django.shortcuts import render
from django.views import View


def home(request):
    return render(request , 'index.html')






