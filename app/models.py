from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.
class DataPoint(models.Model):
        device = models.ForeignKey("Device", null=True, on_delete=models.SET_NULL)
        time_stamp = models.IntegerField()
        loc = models.CharField(max_length=14)
        temp = models.DecimalField(max_digits=4, decimal_places=1)
        hum = models.DecimalField(max_digits=4, decimal_places=1)
        bar = models.DecimalField(max_digits=5, decimal_places=1)
        lux = models.DecimalField(max_digits=5, decimal_places=1)

        def save(self, *args, **kwargs):
            device = Device.objects.get(id=self.device_id)
            device.current_time_stamp = self.time_stamp
            device.current_luc = self.loc
            device.current_temp = self.temp
            device.current_hum = self.hum
            device.current_bar = self.bar
            device.current_lux = self.lux
            device.save()
            super(DataPoint, self).save(*args, **kwargs)


class Device(models.Model):
        location = models.ForeignKey("Location", null=True, on_delete=models.SET_NULL)
        focus = models.BooleanField(default=False)
        current_time_stamp = models.IntegerField(default=1)
        current_loc = models.CharField(max_length=14, blank=True)
        current_temp = models.DecimalField(max_digits=4, default=1, decimal_places=1)
        current_hum = models.DecimalField(max_digits=4, default=1, decimal_places=1)
        current_bar = models.DecimalField(max_digits=5, default=1, decimal_places=1)
        current_lux = models.DecimalField(max_digits=5, default=1, decimal_places=1)

        def toggle_focus(self):
            self.focus = not self.focus
            return self.focus

        def __str__(self):
            return "blik unit #" + str(self.id)


class Location(models.Model):
        name = models.CharField(max_length=40)
        slug = models.SlugField(max_length=40, blank=True, unique=True)
        allowed_users = models.ManyToManyField(User)
        focus = models.BooleanField(default=False)

        def toggle_focus(self):
            self.focus = not self.focus
            return self.focus

        def save(self, *args, **kwargs):
            slug = slugify(self.name)
            super(Location, self).save(*args, **kwargs)

        def __str__(self):
            return self.name

# Class User automatically created
