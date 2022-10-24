from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie2
# Create your views here.

def Movie2_view(request):
    movie2 = Movie2.objects.all()
    return HttpResponse(request)
