# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalassignmentapp', '0008_auto_20170115_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lists',
            old_name='li_usernaam',
            new_name='li_username',
        ),
        migrations.AlterField(
            model_name='order',
            name='or_listid',
            field=models.IntegerField(default=0),
        ),
    ]
