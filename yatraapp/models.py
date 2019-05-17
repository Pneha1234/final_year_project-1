from django.db import models
import datetime
from django.utils import timezone


class Food(models.Model):
    food_image_url = models.CharField(max_length=600, null=True)
    location = models.CharField(max_length = 50, null=True)
    food_name = models.CharField(max_length = 50, null=True)
    description = models.CharField(max_length = 200, null=True)
    category = models.CharField(max_length = 500, null=True)
    checkin = models.DateField(default=timezone.now)
    checkout = models.DateField(default=timezone.now)


class Festival(models.Model):
    festival_image_url = models.CharField(max_length=600, null=True)
    location = models.CharField(max_length=50, null=True)
    festival_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    ethinic = models.CharField(max_length=100, null=True)
    month = models.CharField(max_length = 60, null=True)


class Event(models.Model):
    location = models.CharField(max_length=50, null=True)
    event_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    month = models.CharField(max_length=60, null=True)
    date_created = models.DateTimeField(default=timezone.now)


