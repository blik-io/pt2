from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Device(models.Model):
        device = models.IntegerField()
        time_stamp = models.IntegerField()
        temp = models.DecimalField(max_digits=4, decimal_places=1)
        hum = models.DecimalField(max_digits=4, decimal_places=1)
        bar = models.DecimalField(max_digits=5, decimal_places=1)
        #id = models.AutoField(primary_key=True)
        #location = models.ForeignField("Location", on_delete=models.SET_NULL)
        focus = models.BooleanField(default=False)

        def __str__(self):
            return self.device

class Location(models.Model):
        slug = models.SlugField(max_length=40)
        focus = models.BooleanField(default=False)

# class DataPoints(models.Model):

# class User automatically created
