# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TracebackLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('traceback_type', models.CharField(default=b'', max_length=100)),
                ('traceback_value', models.CharField(default=b'', max_length=200)),
                ('traceback', models.TextField(max_length=2000)),
                ('crawl', models.CharField(max_length=100)),
                ('detail_url', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': '\u9519\u8bef\u8ddf\u8e2a',
                'verbose_name_plural': '\u9519\u8bef\u8ddf\u8e2a',
            },
        ),
    ]
