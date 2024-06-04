from django.shortcuts import render
from .models import *

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def movie_detail(request, _id):
    movie = Movie.objects.filter(id=_id).first()
    actors = movie.actors.all()
    return render(request, 'movie_detail.html', {'movie': movie, 'actors': actors})

