from urllib import request
from uuid import uuid4
import uuid
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from base.models import Profile, Movie, Tvshows
from .forms import ProfileForm
from django.views import View




def home(request):
    if request.user.is_authenticated:
        return redirect('profile')

    return render(request , 'index.html')


@login_required(login_url='account_login') 
def profile(request):
    profiles = request.user.profiles.all()
    return render(request,'profileList.html' , {
        'profiles' : profiles
    })

@method_decorator(login_required, name='dispatch') 

class CreateProfile(View):

    def get(self,request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'profileCreate.html', {
            'form' : form
        })

    def post(self,request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
           profile = Profile.objects.create(**form.cleaned_data)
           if profile:
               request.user.profiles.add(profile)
               return redirect('profile')

        return render(request, 'profileCreate.html', {
            'form' : form
        })

@login_required(login_url='account_login') 
def WatchStuff(request, id):
    try:
        profile = Profile.objects.get(uuid=id)
        movies = Movie.objects.all()
        tvshows = Tvshows.objects.all()

        if profile not  in request.user.profiles.all():
            return redirect('profile')
        return render(request,'watchList.html',{
            'movies': movies,
            'tvshows': tvshows
        }) 

    except print('errr'):
        return redirect('profile')
            
def ShowDetails(request, id):
   
        if Movie.objects.get(id=id):
            movie = Movie.objects.get(id=id)
            def movie_genre(self):
                 return ', '.join([a.movie_genre for a in self.Movie.all()])
            return render(request,'Details.html',{
            'movie': movie,
        }) 
        elif Tvshows.objects.get(id=id):
            tvshow=  tvshow = Tvshows.objects.get(id=id)
            return render(request,'Details.html',{
            'tvshow': tvshow,
        }) 
        else:
            return redirect('profile')






