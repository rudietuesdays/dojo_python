# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0003_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='liked',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
