# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from front.models import Request as req
from front.models import Response as res
from django.core import serializers

# Create your views here.
def index(request):
    addedData = req.objects.all().order_by('-id')[:10]
    return render(request, 'dashboard.html', {'data': addedData})

def add(request):
    addedData = req.objects.all().order_by('-id')[:10]
    return render(request, 'add.html', {'data': addedData})

def update(request):
    return render(request, 'update.html', {})


def ajax(request):
    soru=request.POST.get('soru')
    sr=req.objects.create(text=soru)
    sr.save()
    cevap=request.POST.get('cevap')
    cvp=res.objects.create(text=cevap,request_id=sr.id)
    cvp.requests.add(sr)
    cvp.save()
    
    return JsonResponse({
        "soru":sr.id,
        "cevap":cvp.id,
    })