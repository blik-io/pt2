from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .models import Device, User

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
                    return HttpResponseRedirect("/")
                else:
                    print("There was a problem activating your account.")
            else:
                print("The username or password were incorrect.")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def focus_device(request):
    device_id = request.POST.get("device_id", None)
    if (device_id):
        device = Device.objects.get(id=int(device_id))
        if device is not None:
            focus = not device.focus
            device.focus = focus
            device.save()
    return HttpResponse(focus)
