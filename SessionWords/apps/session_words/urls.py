from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^word$', views.process),
    url(r'^clear$', views.clear),
]