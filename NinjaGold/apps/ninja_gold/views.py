# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
import time

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    else:
        request.session['gold'] += 0
    if 'place' not in request.session:
        request.session['place'] = ''
    else:
        request.session['place'] += ''
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    giveOrTake = random.randint(0, 1)
    if request.POST['building'] == 'farm':
        farm = random.randint(10, 20)
        request.session['place'] = 'Earned ' + str(farm) + ' golds from the farm! ' + '(' + time.ctime() + ')'
        request.session['gold'] += farm
    elif request.POST['building'] == 'cave':
        farm = random.randint(5, 10)
        request.session['place'] = 'Earned ' + str(farm) + ' golds from the cave! ' + '(' + time.ctime() + ')'
        request.session['gold'] += farm
    elif request.POST['building'] == 'house':
        farm = random.randint(2, 5)
        request.session['place'] = 'Earned ' + str(farm) + ' golds from the house! ' + '(' + time.ctime() + ')'
        request.session['gold'] += farm
    elif request.POST['building'] == 'casino':
        if giveOrTake == 0:
            farm = random.randint(0, 50)
            request.session['place'] = 'Entered a casino and lost ' + str(farm) + ' golds...Ouch.. ' + '(' + time.ctime() + ')'
            request.session['gold'] -= farm
        else:
            farm = random.randint(0, 50)
            request.session['place'] = 'Entered a casino and won ' + str(farm) + ' golds! ' + '(' + time.ctime() + ')'
            request.session['gold'] += farm
    return redirect('/')