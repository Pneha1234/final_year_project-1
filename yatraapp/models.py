from django.db import models
from month.models import MonthField
import datetime
from django.utils import timezone


class Food(models.Model):
    location = models.CharField(max_length = 50)
    food_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    category = models.CharField(max_length = 500)
    month = MonthField("Month Value")


class Festival(models.Model):
    location = models.CharField(max_length=50)
    festival_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ethinic = models.CharField(max_length=100)
    month = MonthField("Month Value")

class Event(models.Model):
    location = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    month = MonthField("Month Value")
    date_created = models.DateTimeField(default=timezone.now)


