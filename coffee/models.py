from django.db import models
from django.db.models.base import ModelState
from django.utils import timezone

from uuid import uuid4
from math import floor

# Create your models here.

def assign_id():
  return uuid4().hex

class Bean(models.Model):
  # auto fields
  created_date = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  slug = models.SlugField(default=assign_id, editable=False)
  
  # mandatory fields
  name = models.CharField(max_length=140)
  country = models.CharField(max_length=100) # Kenya
  supplier = models.CharField(max_length=50) # Sweet Maria's
  supplier_website = models.URLField(max_length=200) # https://www.sweetmarias.com/guatemala-xinabajul-producers-6856.html
  delivered_on = models.DateField() # 12 October 2021

  # optional fields
  photo = models.ImageField(upload_to="uploads/", blank=True, null=True)
  description = models.TextField(blank=True)
  region = models.CharField(max_length=140, blank=True) # Kiambu County Mt. Kenya, Central Kenya
  variety = models.CharField(max_length=140, blank=True) # Multiple
  process = models.CharField(max_length=100, blank=True) # Washed
  harvest = models.CharField(max_length=140, blank=True) # February - March & November - December
  drying = models.CharField(max_length=100, blank=True) # Sun Dried
  altitude_min = models.PositiveIntegerField(blank=True, null=True, default=0) # 1400
  altitude_max = models.PositiveIntegerField(blank=True, null=True, default=0) # 2000

  decaffeinated = models.BooleanField(default=False) # False
  certified_organic = models.BooleanField(default=False) # False
  certified_fairtrade = models.BooleanField(default=False) # False
  certified_rainforestalliance = models.BooleanField(default=False) # False

  class Meta:
    ordering = ['-delivered_on']

  def get_url(self):
    return f"/beans/{self.slug}"

  def get_roasts(self):
    roasts = Roast.objects.filter(bean=self.id)
    return roasts

  def __str__ (self):
    date = self.delivered_on.strftime("%b-%Y")
    return f'{self.name} ({date} {self.supplier})'

class Roast(models.Model):
  # auto fields
  created_date = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  slug = models.SlugField(default=assign_id, editable=False)

  # mandatory fields
  bean = models.ForeignKey(Bean, blank=False, on_delete=models.CASCADE)
  green_quantity = models.DecimalField(help_text="Starting weight in grams", max_digits=5, decimal_places=1)
  roast_quantity = models.DecimalField(help_text="Yield weight in grams", max_digits=5, decimal_places=1)
  roaster = models.CharField(max_length=255, default="Behmor 2000AB Plus")
  time_to_first_crack = models.PositiveIntegerField(help_text="Time to first crack in seconds")
  time_to_cooling = models.PositiveIntegerField(help_text="Time to cooling in seconds")
  roasted_on = models.DateTimeField() # default to current time? , change to DateField
  degree_of_roast = models.CharField(max_length=140) # Full City

  roast_log = models.FileField(upload_to='uploads/')

  class Meta:
    ordering = ['-roasted_on']

  def get_url(self):
    return f"/roasts/{self.slug}"

  def days_since_roast(self):
    diff = timezone.now() - self.roasted_on
    return round(diff.total_seconds() / (60*60*24))

  def weight_loss(self):
    q1 = self.green_quantity
    q2 = self.roast_quantity
    return round((q1-q2)/q1*100, 1)

  def roast_time(self):
    mm = floor(self.time_to_cooling / 60)
    ss = str(self.time_to_cooling % 60).zfill(2)
    return f'{mm}:{ss}'

  def time_past_first_crack(self):
    diff = self.time_to_cooling - self.time_to_first_crack
    mm = floor(diff / 60)
    ss = str(diff % 60).zfill(2)
    return f'{mm}:{ss}'

  def __str__ (self):
    date = self.roasted_on.strftime("%d %b %Y")
    return f'{date} ({self.bean.name} - {self.degree_of_roast})'


class File(models.Model):
  # auto fields
  created_date = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  slug = models.SlugField(default=assign_id, editable=False)

  display_name = models.CharField(max_length=255)
  file = models.FileField(upload_to='files/')

  def __str__(self):
    date = self.last_modified.strftime("%d %b %Y")
    return f'{self.file} ({date})'