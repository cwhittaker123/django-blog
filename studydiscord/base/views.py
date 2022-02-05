from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request : HttpRequest):
    return render(request, 'home.html')

def room(request : HttpRequest):
    return render(request, 'room.html')