# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'total' not in request.session:
        request.session['total'] = []
    return render(request, 'amadon/index.html')

def buy(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
        request.session['price'] = (float(request.POST['price']) * float(request.POST['quantity']))
        request.session['quantity'] = request.POST['quantity']
        request.session['total'].append(request.session['price'])

    sum = 0.0
    for prices in request.session['total']:
       sum += float(prices)
    
    request.session['sum'] = sum

    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')
