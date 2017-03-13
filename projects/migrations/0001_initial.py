# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoubanSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('url', models.CharField(default=b'', max_length=200)),
                ('image_url', models.CharField(default=b'', max_length=300)),
                ('directors', models.CharField(default=b'', max_length=300)),
                ('actors', models.CharField(default=b'', max_length=300)),
            ],
            options={
                'verbose_name': '\u8c46\u74e3\u4e3b\u9898',
                'verbose_name_plural': '\u8c46\u74e3\u4e3b\u9898',
            },
        ),
    ]
