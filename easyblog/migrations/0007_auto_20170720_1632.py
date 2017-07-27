# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyblog', '0006_auto_20170720_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='catogory_created_time',
        ),
        migrations.RemoveField(
            model_name='category',
            name='catogory_last_modified_time',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='easyblog.Tag'),
        ),
    ]
