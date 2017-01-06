from django.contrib import admin
from .models import Device, Location, DataPoint

# Register your models here.
admin.site.register(Device)
admin.site.register(Location)
admin.site.register(DataPoint)
