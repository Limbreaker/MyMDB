from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView, DetailView


class MovieList(ListView):
    model = Movie
    paginate_by = 10


class MovieDetail(DetailView):
    model = Movie


#for z in range(150):
    #Movie.objects.create(
        #title='Title {}'.format(z),
        #year=1990 + z,
        #runtime=100,)