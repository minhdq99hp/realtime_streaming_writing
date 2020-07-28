from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.

# class LoginView():
#     template_name='login.html'

# class SignUpView():
#     template_name='signup.html'

class RoomListView(ListView): #Home
    template_name='home.html'
    
class RoomDetailView(DetailView):
    template_name='room_detail.html'