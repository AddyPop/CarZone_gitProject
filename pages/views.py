from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'home.html', context=data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'about.html', context=data)

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def car(request):
    return render(request, 'car.html')