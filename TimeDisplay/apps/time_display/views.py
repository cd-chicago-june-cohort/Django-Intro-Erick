# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    info = {
        'time' : strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', info)


