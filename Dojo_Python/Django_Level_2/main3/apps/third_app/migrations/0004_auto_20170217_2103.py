# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0003_auto_20170217_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=255),
        ),
    ]
