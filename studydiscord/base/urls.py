"""studydiscord base URL Configuration"""
from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"), # dynamic value of type str <str:pk>
]