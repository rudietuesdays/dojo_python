# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0004_auto_20170217_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
