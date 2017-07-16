# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    if 'wordList' not in request.session:
        request.session['wordList'] = []
    return render(request, 'session_words/index.html')

def process(request):
    if request.method == 'POST':
        word = request.POST['wordEntered']
        color = request.POST['color']
        if 'fontSize' in request.POST:
            font = 30
        else:
            font = 20

        info = {
            'word' : word,
            'color' : color,
            'font' : font,
            'time' : strftime("%Y-%m-%d %H:%M %p", gmtime())
        }
        request.session['wordList'].append(info)
        request.session.modified = True
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    request.session['wordList'] = []
    return redirect('/')

