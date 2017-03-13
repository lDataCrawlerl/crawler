# coding: utf-8

from django.contrib import admin
from .models import DoubanSubject


@admin.register(DoubanSubject)
class DoubanSubjectAdmin(admin.ModelAdmin):
    pass
