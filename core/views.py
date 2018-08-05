from django.shortcuts import render
from .models import Movie, Person
from django.views.generic import ListView, DetailView


class MovieList(ListView):
    model = Movie
    paginate_by = 10


class MovieDetail(DetailView):
    model = Movie


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()


#for z in range(150):
    #Movie.objects.create(
        #title='Title {}'.format(z),
        #year=1990 + z,
        #runtime=100,)