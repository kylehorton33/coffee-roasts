from django.shortcuts import render
from .models import Bean, Roast

from django.views.generic import ListView

from django.utils import timezone
from django.views.generic.detail import DetailView

# Create your views here.
class RoastListView(ListView):
  model = Roast

class BeanListView(ListView):
  model = Bean

class RoastDetailView(DetailView):
  model = Roast

class BeanDetailView(DetailView):
  model = Bean

  

