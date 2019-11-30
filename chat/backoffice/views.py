# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(response):
    return HttpResponse('test')

def add(response):
    return HttpResponse('response')