# coding: utf-8

from common.models import Base
from django.db import models


class DoubanSubject(Base, models.Model):
    url = models.CharField(max_length=200, default='')
    image_url = models.CharField(max_length=300, default='')
    directors = models.CharField(max_length=300, default='')
    actors = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = verbose_name_plural = u'豆瓣主题'
