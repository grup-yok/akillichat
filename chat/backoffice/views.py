# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from front.models import Request as req
from front.models import Response as res

# Create your views here.
def index(request):
    return render(request, 'dashboard.html', {})

def add(request):
    return render(request, 'add.html', {})

def update(request):
    return render(request, 'update.html', {})


def ajax(request):
    soru=request.POST.get('soru')
    sr=req.objects.create(text=soru)
    sr.save()
    cevap=request.POST.get('cevap')
    cvp=res.objects.create(text=cevap,id=sr.id)
    cvp.save()
    return JsonResponse({
        'soru':sr,
        'cevap':cvp,
    })
