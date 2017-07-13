from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^numbers/(?P<number>\d+)$', views.number),
    url(r'^numbers/(?P<number>\d+)/edit$', views.edit),
    url(r'^numbers/(?P<number>\d+)/delete$', views.destroy),
]