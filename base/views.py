from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# Views contain logic and inject dynamic data into rendered templates
# They receive an HttpRequest and return a HttpResponse

rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Design'},
    {'id': 3, 'name': 'Frontend Devs'},
]

def home(request : HttpRequest) -> HttpResponse:
    # Access rooms variable
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request : HttpRequest, pk : str) -> HttpResponse:
    room = None
    for rm in rooms:
        if rm.get('id') == int(pk):
            room = rm
    context = {'room': room}
    return render(request, 'base/room.html', context)