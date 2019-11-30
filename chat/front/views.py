# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import nltk, string
import nltk.corpus
from nltk.tokenize import word_tokenize, sent_tokenize, SpaceTokenizer
from nltk import pos_tag, ne_chunk
#from nltk.probability import FreqDist
from nltk.util import bigrams, trigrams, ngrams
from fuzzywuzzy import fuzz
from front.models import Request as req
from front.models import Response as res
from front.models import Dictionary as dic
from googlesearch import search

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def messageReceive(request):
    message = request.POST.get('message')
    ms = req.objects.create(text=message)
    ms.save()

    AI_tokens = word_tokenize(message)

    #tok = SpaceTokenizer()
    #toks = tok.tokenize(message)
    #pos = pos_tag(toks)
    #chunked_nes = ne_chunk(pos) 
    #nes = [' '.join(map(lambda x: x[0], ne.leaves())) for ne in chunked_nes if isinstance(ne, nltk.tree.Tree)]

    response = ""

    for word in AI_tokens:
        findDic = dic.objects.filter(word__contains=word)
        if len(findDic) <= 0:
            wrd = dic.objects.create(word=prounancationFixer(word))
            wrd.save()
        

        findreq = res.objects.filter(text__contains=word)
        for x in findreq:
            rat = fuzz.token_set_ratio(x.text, word)
            if rat >= 90:
                response = x.text


    return JsonResponse({
        "message": response
    })

def googleSearch(query):
    result = []
    for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
        result.append(i)
    return result


def prounancationFixer(text):
    prounList = ['nın', 'nin', 'nun', 'nün', 'ün', 'ın', 'un', 'ni', 'nu', 'nü', 'nı']

    for pron in prounList:
        if pron in text:
            text = text.rstrip(pron)

    return text