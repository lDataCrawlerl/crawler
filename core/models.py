# coding: utf-8

from django.db import models


class TracebackLog(models.Model):

    traceback_type = models.CharField(max_length=100, default='')
    traceback_value = models.CharField(max_length=200, default='')
    traceback = models.TextField(max_length=2000)
    crawl = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=500)

    class Meta:
        verbose_name = verbose_name_plural = u'错误跟踪'
