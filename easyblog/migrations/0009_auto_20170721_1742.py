# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyblog', '0008_auto_20170720_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_time']},
        ),
    ]
