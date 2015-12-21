# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 12, 16, 17, 6, 58, 564410, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 16, 17, 7, 7, 962179, tzinfo=utc)),
            preserve_default=False,
        ),
    ]