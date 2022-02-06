"""studydiscord base URL Configuration"""
from django.urls import path
from base import views

urlpatterns = [
    # Access the path by using the name supplied
    # Use a name so that the urls can change and we don't have to change them throughout the app
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"), # dynamic value of type str <str:pk>
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
]