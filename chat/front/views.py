# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import nltk, string
import nltk.corpus
from nltk.tokenize import word_tokenize, sent_tokenize
#from nltk.probability import FreqDist
from nltk.util import bigrams, trigrams, ngrams
from fuzzywuzzy import fuzz
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

    response = ""

    for word in AI_tokens:
        wrd = dic.objects.create(word=word)
        wrd.save()

        findreq = res.objects.filter(text__contains=word)
        print(findreq)
        for x in findreq:
            rat = fuzz.token_set_ratio(x.text, word)
            if rat >= 90:
                response = x.text


    return JsonResponse({
        "message": response
    })