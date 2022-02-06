from typing import final
from urllib import request
from uuid import uuid4
import uuid
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from base.models import Episode, Profile, Movie, Tvshows
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
        episode = Episode.objects.all()
        tvshow = Tvshows.objects.get(title="Breaking Bad")
        
        

        if profile not  in request.user.profiles.all():
            return redirect('profile')
        return render(request,'watchList.html',{
            'movies': movies,
            'episode': episode,
            'tvshow': tvshow,
           
        }) 

    except print('errr'):
        return redirect('profile')
            
@login_required(login_url='account_login')             
def ShowDetails(request, id):
    
        try:
            page = 'movie'
            movie = Movie.objects.get(uuid=id)
            genres = movie.genre.all()
            return render(request,'Details.html',{
            'movie': movie,
            'genres':genres,
            'page': page
            }) 
        except  Movie.DoesNotExist:
               episode =Episode.objects.get(uuid=id)
               genres = episode.Tvshow.genre.all()
               return render(request,'Details.html',{
                'episode': episode,
                'genres':genres,
                }) 
                


         
        
    


@login_required(login_url='account_login')   
def PlayStuff(request, id):
    try:
            movie = Movie.objects.get(uuid=id)
            movie = movie.video.values()
            return render(request,'showStuff.html',{
            'movie': list(movie),
        }) 
    except  Movie.DoesNotExist:
            episode = Episode.objects.get(uuid=id)
            episode = episode.video.values()
            return render(request,'showStuff.html',{
            'episode': list(episode),
        }) 
  





