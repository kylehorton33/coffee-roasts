from django.db import models
from django.shortcuts import render
from .models import Bean, Roast, File

from django.views.generic import ListView

from django.utils import timezone
from django.views.generic.detail import DetailView

from .forms import NewRoastModelForm
from django.views.generic.edit import FormView

# Create your views here.
class RoastListView(ListView):
  model = Roast

class RoastCreate(FormView):
  template_name = 'roast/new.html'
  form_class = NewRoastModelForm
  success_url = '/'

  def form_valid(self, form):
    form.save()
    return super(RoastCreate, self).form_valid(form)

class BeanListView(ListView):
  model = Bean
  paginate_by = 10

class RoastDetailView(DetailView):
  model = Roast

class BeanDetailView(DetailView):
  model = Bean

class FileListView(ListView):
  model = File
  

