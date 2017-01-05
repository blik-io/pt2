from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Static pages
    # Does not work with forms, or translation. Also bad idea if audience targeting is wanted
    url(r'^$', TemplateView.as_view(template_name="templates/index.html"), name = "index"),
]
