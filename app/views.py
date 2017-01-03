from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    device = "Sensor 1"
    temp = 20.0
    hum = 45.5
    bar = 989.7

    context = {"device": device,
    "temperature": temp,
    "humidity": hum,
    "pressure": bar}

    return render(request, "index.html", {"devices":devices})


class Device:
    def __init__(self, id, time_stamp, temp, hum, bar):
        self.id = id
        self.time_stamp = time_stamp
        self.temp = temp
        self.hum = hum
        self.bar = bar

devices = [
    Device(1, 12, 20.2, 45.5, 989.7),
    Device(3, 12, 20.0, 55.2, 923.9),
    Device(7, 15, 22.6, 43.6, 1011.1),
    Device(1, 16, 20.3, 47.3, 998.4)
]
