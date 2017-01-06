from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from .forms import LoginForm
from .models import Device, User

# Create your views here.
def index(request):
    # strongly a mockup
    devices = Device.objects.all()
    return render(request, "devices.html", {"devices":devices})

def devices(request):
    devices = Device.objects.all()
    return render(request, "devices.html", {"devices":devices})

def device(request, device_id):
    device = Device.objects.get(id=device_id)
    return render(request, "device.html", {"device":device})

def locations(request):
    # obviously a mockup
    locations = Device.objects.all()
    return render(request, "devices.html", {"device":locations})

def location(request, slug):
    # obviously a mockup
    location = Location.objects.get(slug=slug)
    return render(request, "location.html", {"location":location})

def alerts(request):
    # obviously a mockup
    request_user = request.user.id
    if request.user.is_authenticated:
        alerts = Alert.objects.get(user=current_user)
        return render(request, "alerts.html", {"alerts":alerts})
    else:
        return redirect(reverse("login", args=[]))

# User Relevant views
def user(request, username):
    user = User.objects.get(username=username)
    # show settings
    # link organisation to user
    return render(request, "user.html", {"username": username})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username = un, password = pw)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse("dashboard", args=[]))
                else:
                    # Raises Error bei inkorrekter Eingabe, muss gefixt werden.
                    print("There was a problem activating your account.")
            else:
                print("The username or password were incorrect.")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect(reverse("login", args=[]))

# Further Website Features
def focus_device(request):
    """
    POSTs an attribute 'focused' to the device. With the focus attribute, a prioritied list of devices shall be created.
    It works together with an ajax function in app.js and some html in devices.html.
    """
    device_id = request.POST.get("device_id", None)
    if (device_id):
        device = Device.objects.get(id=int(device_id))
        if device is not None:
            focus = not device.focus
            device.focus = focus
            device.save()
    return HttpResponse(focus)
