# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendsList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_1', to='friendsList.Friend')),
                ('friend_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_2', to='friendsList.Friend')),
            ],
        ),
    ]