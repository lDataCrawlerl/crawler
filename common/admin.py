# coding: utf-8

from django.contrib import admin


class CreatedUpdatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
