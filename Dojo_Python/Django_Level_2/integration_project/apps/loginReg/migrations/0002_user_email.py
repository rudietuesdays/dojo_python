# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
