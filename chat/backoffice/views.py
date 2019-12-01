# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request):
    return render(request, 'dashboard.html', {})

def add(request):
    return render(request, 'add.html', {})

def update(request):
    return render(request, 'update.html', {})


def ajax(request):
    return JsonResponse({})
