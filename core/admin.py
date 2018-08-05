from django.contrib import admin
from .models import Movie, Person, PersonManager


admin.site.register(Movie)
admin.site.register(Person)