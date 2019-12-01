# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Request(models.Model):
    text = models.CharField(max_length=1000)

class Response(models.Model):
    text = models.CharField(max_length=1000)
    request_id = models.IntegerField(default=0)
    requests = models.ManyToManyField(Request)

class Dictionary(models.Model):
    request_id = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    word = models.CharField(max_length=1000)
    