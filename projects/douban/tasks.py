# coding: utf-8

import time
from __future__ import absolute_import, unicode_literals
# from common.utils import parse_doc
from celery import shared_task, task


@task
def parse_subject(page):
    # doc = parse_doc(page)
    # print doc
    print page


@shared_task()
def dispatch_douban_subject_task():
    for start in range(0, 100, 10):
        # print start
        parse_subject.delay(start)
