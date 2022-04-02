from django.shortcuts import render
from .models import *

def base(request):
        return render(request, 'base.html')

def example(request):
    populations = Population.objects.all()
    context = {
        'populations' : populations
    }
    return render(request, 'examp.html', context)

def index(request):
    areas = Area.objects.all()
    context = {
        'areas' : areas
    }
    return render(request, 'index.html', context)

def yaim(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'yaim.html', context)