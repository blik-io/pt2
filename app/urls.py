from django.conf.urls import url
from . import views

urlpatterns = [
    # Main app
    url(r'^$', views.index, name = "index"),
    url(r'^dashboard/$', views.index, name = "dashboard"),
    url(r'^devices/$', views.devices, name = "devices"),
    url(r'^devices/([0-9]+)/', views.device, name = "device"),
    url(r'^locations/$', views.locations, name = "locations"),
    url(r'^locations/([a-z0-9-]+)/', views.location, name = "location"),
    url(r'^alerts/$', views.alerts, name = "alerts"),

    # User management
    url(r'^user/(\w+)/', views.user, name="user"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),

    # Focus button
    url(r'focus_device/$', views.focus_device, name="focus_device"),
]
