import django
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from base.models import Room, Topic
from base.forms import RoomForm

# Create your views here.
# Views contain logic and inject dynamic data into rendered templates
# They receive an HttpRequest and return a HttpResponse

# rooms = [
#     {'id': 1, 'name': 'Learn Python'},
#     {'id': 2, 'name': 'Design'},
#     {'id': 3, 'name': 'Frontend Devs'},
# ]

# Call this loginPage bc login() is a built in function
def loginPage(request : HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exist
        try:
            user = User.objects.get(username=username)
        except:
            # Pass message to template
            messages.error(request, 'User does not exist')

        # If user does exist, try to authenticate. Returns None if creds are invalid
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Add session to db and store in browser as cookie
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request : HttpRequest) -> HttpResponse:
    # Logout user by deleting session token in db and browser
    logout(request)
    return redirect('home')

def home(request : HttpRequest) -> HttpResponse:
    # queryset = ModelName.objects.all()/.get()/.filter()/.exclude()
    # get all rooms in the db
    # Get the url param q
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # Whatever value is in topic name can match if it's a subset, i means case insenitve
    # Ex: Py would match Python
    rooms = Room.objects.all().filter(
        # Search by topic name, room name, room description
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    # get all topics in the db
    topics = Topic.objects.all()

    # get count of the rooms, works faster than len()
    room_count = rooms.count()

    # Access rooms variable
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
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

def updateRoom(request: HttpRequest, pk : str) -> HttpResponse:
    """Update a Room by id"""
    room = Room.objects.get(id=pk)

    # Prefill form with room values
    form = RoomForm(instance=room)

    if request.method == 'POST':
        # Process request post info and update the existing room
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request: HttpRequest, pk : str) -> HttpResponse:
    """Delete a room by id"""
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})