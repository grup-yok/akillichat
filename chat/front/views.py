# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import nltk, string
import nltk.corpus
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams, trigrams, ngrams
from front.models import Request as req
from front.models import Response as res
from front.models import Dictionary as dic

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def messageReceive(request):
    message = request.POST.get('message')
    ms = req.objects.create(text=message)
    ms.save()

    AI_tokens = word_tokenize(message)

    fdist = FreqDist()
    for word in AI_tokens:
        fdist[word.lower()]+=1
        wrd = dic.objects.create(word=word)
        wrd.save()
    fdist

    biagram = list(nltk.bigrams(AI_tokens))
    return JsonResponse({
        "message": ""
    })