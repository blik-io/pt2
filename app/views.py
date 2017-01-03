from django.shortcuts import render
from .models import Device

# Create your views here.
def index(request):
    devices = Device.objects.all()
    return render(request, "devices.html", {"devices":devices})

def devices(request):
    devices = Device.objects.all()
    return render(request, "devices.html", {"devices":devices})

def device(request, device_id):
    device = Device.objects.get(id=device_id)
    return render(request, "device.html", {"device":device})
