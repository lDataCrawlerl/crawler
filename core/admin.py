# coding: utf-8

from django.contrib import admin
from .models import TracebackLog


@admin.register(TracebackLog)
class TracebackLogAdmin(admin.ModelAdmin):
    search_fields = ('crawl', 'traceback_type')
