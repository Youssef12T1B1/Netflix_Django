from unicodedata import name
from django import views
from django.urls import path
from . import views
from  .views import CreateProfile

urlpatterns = [

    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/create', CreateProfile.as_view(), name='CreateProfile'),
    path('watch/<str:id>/', views.WatchStuff, name='WatchStuff'),
    path('details/<str:id>/', views.ShowDetails, name='ShowDetails'),
    path('play/<str:id>/', views.PlayStuff, name='PlayStuff'),

 
]
