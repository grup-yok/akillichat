# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams, trigrams, ngrams

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def messageReceive(request):
    message = request.POST.get('message')
    AI_tokens = word_tokenize(message)
    fdist = FreqDist()
    for word in AI_tokens:
        fdist[word.lower()]+=1
    fdist

    biagram = list(nltk.bigrams(AI_tokens))
    return JsonResponse({
        "message": biagram
    })