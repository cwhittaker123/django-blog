from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request : HttpRequest):
    return HttpResponse('Home Page')

def room(request : HttpRequest):
    return HttpResponse('ROOM')