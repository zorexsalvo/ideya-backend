# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Problem)
admin.site.register(Solution)

admin.site.site_header = 'Ideya Administration'
