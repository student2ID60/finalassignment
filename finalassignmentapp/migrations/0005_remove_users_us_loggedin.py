# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalassignmentapp', '0004_auto_20170114_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='us_loggedin',
        ),
    ]
