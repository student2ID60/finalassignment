# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalassignmentapp', '0005_remove_users_us_loggedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='us_loggedin',
            field=models.BooleanField(default=False),
        ),
    ]
