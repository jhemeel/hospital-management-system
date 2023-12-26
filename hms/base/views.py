from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from doctors.models import Doctor

# Create your views here.

class Home(ListView):
    model = Doctor
    template_name = 'base/home.html'