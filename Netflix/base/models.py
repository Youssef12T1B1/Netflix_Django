from pickle import TRUE
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 
Age_Choises= (
    ('+18','+18'),
    ('Kid','Kid')

)


class maUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', related_name='Profiles', blank=True)
    


class Profile(models.Model):
    username = models.CharField(max_length=200)
    age_limit = models.CharField(max_length=200, choices=Age_Choises)
    uuid = models.UUIDField(default=uuid.uuid4)



class Geners(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Rate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True) 
    file = models.FileField(upload_to='Videos')   

class Movie(models.Model):
    title = models.CharField(max_length=200)
    Storyline = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Geners, related_name='Genres', blank=True )
    year= models.CharField(max_length=10,null=True)
    poster = models.ImageField(upload_to ='Posters') 
    rating = models.ForeignKey(Rate, on_delete=models.SET_NULL , null=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    video = models.ManyToManyField(Video)

class Season(models.Model):
    episodes = models.ManyToManyField('Episode', related_name='Episode', blank=True)
    description = models.TextField(blank=True, null=True)
    number = models.CharField(max_length=10)
    tvshow = models.ForeignKey('Tvshows', on_delete=models.CASCADE)

class Episode(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    number = models.CharField(max_length=10)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    Tvshow = models.ForeignKey('Tvshows', on_delete=models.CASCADE)

Statu_Choises = (
    ('completed', 'Completed'),
    ('Ongoing', 'Ongoing')
) 
class Tvshows(models.Model):
    seasons = models.ManyToManyField(Season, related_name='Seasons', blank=True)
    episodes = models.ManyToManyField(Episode, related_name='Episodes', blank=True)
    title = models.CharField(max_length=200)
    Storyline = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Geners, related_name='Tv_Genres', blank=True )
    year= models.CharField(max_length=10,null=True)
    poster = models.ImageField(upload_to ='Posters') 
    rating = models.ForeignKey(Rate, on_delete=models.SET_NULL , null=True)
    Status = models.CharField(max_length=200, choices=Statu_Choises , null=True)





