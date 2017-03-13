# coding: utf-8

from django.contrib import admin
from .models import DoubanSubject
from common.admin import CreatedUpdatedAdmin


@admin.register(DoubanSubject)
class DoubanSubjectAdmin(CreatedUpdatedAdmin):
    pass
