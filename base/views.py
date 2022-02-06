from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from base.models import Room
from base.forms import RoomForm

# Create your views here.
# Views contain logic and inject dynamic data into rendered templates
# They receive an HttpRequest and return a HttpResponse

# rooms = [
#     {'id': 1, 'name': 'Learn Python'},
#     {'id': 2, 'name': 'Design'},
#     {'id': 3, 'name': 'Frontend Devs'},
# ]

def home(request : HttpRequest) -> HttpResponse:
    # queryset = ModelName.objects.all()/.get()/.filter()/.exclude()
    # get all rooms in the db
    rooms = Room.objects.all()
    # Access rooms variable
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request : HttpRequest, pk : str) -> HttpResponse:
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request: HttpRequest) -> HttpResponse:
    form = RoomForm()
    if request.method == 'POST':
        # Pass in all the values from the POST data to the RoomForm
        form = RoomForm(request.POST)
        # If all values are correct, save model in DB and send user to home page
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)