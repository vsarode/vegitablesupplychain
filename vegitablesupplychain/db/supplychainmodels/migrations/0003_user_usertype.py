# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-30 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainmodels', '0002_auto_20190330_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('FARMER', 'FARMER'), ('HOTEL', 'HOTEL')], default=None, max_length=512),
            preserve_default=False,
        ),
    ]
