from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Design'},
    {'id': 3, 'name': 'Frontend Devs'},
]

def home(request : HttpRequest):
    # Access room variable
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request : HttpRequest):
    return render(request, 'base/room.html')