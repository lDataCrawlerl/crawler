# coding: utf-8

from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(verbose_name=u'修改时间', auto_now=True, editable=True)

    class Meta:
        abstract = True

