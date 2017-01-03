from django.shortcuts import render
from .models import Device

# Create your views here.
def index(request):
    devices = Device.objects.all()
    return render(request, "index.html", {"devices":devices})

#devices = [
#    Device(device = 1, time_stamp = 12, temp = 20.2, hum = 45.5, bar = 989.7),
#    Device(device = 3, time_stamp = 12, temp = 20.0, hum = 55.2, bar = 923.9),
#    Device(device = 7, time_stamp = 15, temp = 22.6, hum = 43.6, bar = 1011.1),
#    Device(device = 1, time_stamp = 16, temp = 20.3, hum = 47.3, bar = 998.4)
#]
