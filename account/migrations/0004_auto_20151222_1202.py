# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='SlackAccount',
        ),
    ]
