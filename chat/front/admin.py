# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Request, Response, Dictionary

admin.site.register(Request)
admin.site.register(Response)
admin.site.register(Dictionary)