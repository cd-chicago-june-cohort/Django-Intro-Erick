# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    randomWord = get_random_string(length=14)
    info = {
        'word' : randomWord,
        'counter' : request.session['counter'] 
    }
    request.session['counter'] += 1
    return render(request, 'random_word/index.html', info)


