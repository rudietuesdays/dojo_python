# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendsList', '0003_auto_20170221_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='friend_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_1', to='friendsList.Friend'),
        ),
    ]
