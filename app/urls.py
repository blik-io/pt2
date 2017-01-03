from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^devices/$', views.devices, name = "devices"),
    url(r'^devices/([0-9]+)/$', views.device, name = "device"),
    #url(r'^locations/$', views.locations, name = "locations"),
    #ulr(r'^locations/([0-9]+)/$', views.location, name = "location"),
]
