from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):
        device = models.IntegerField()
        time_stamp = models.IntegerField()
        temp = models.DecimalField(max_digits=4, decimal_places=1)
        hum = models.DecimalField(max_digits=4, decimal_places=1)
        bar = models.DecimalField(max_digits=5, decimal_places=1)
        #id = models.AutoField(primary_key=True)

        def __str__(self):
            return self.device
