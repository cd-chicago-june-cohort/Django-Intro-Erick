# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def number(request, number):
    return HttpResponse(number)

def edit(request, number):
    return HttpResponse('placeholder to edit blog ' + str(number))

def destroy(request, number):
    return redirect('/blogs')