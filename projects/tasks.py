# coding: utf-8

from __future__ import absolute_import, unicode_literals
import time
# from common.utils import parse_doc
from celery import shared_task, task


@task()
def parse_subject(page):
    # doc = parse_doc(page)
    # print doc
    print 'start', page
    time.sleep(10)
    print 'end', page


@shared_task()
def dispatch_douban_subject_task():
    for start in range(0, 100, 10):
        parse_subject(start)
