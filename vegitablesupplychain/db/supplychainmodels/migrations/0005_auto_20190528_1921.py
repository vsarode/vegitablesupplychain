# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-28 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainmodels', '0004_auto_20190528_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellorders',
            name='quality',
            field=models.CharField(default=b'Good', max_length=10),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_token',
            field=models.CharField(default=b'bbe6f876-d3bc-4be1-b886-7773c2fa4330', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchaseorders',
            name='purchase_order_token',
            field=models.CharField(default=b'0d75990c-c4e2-441f-b225-0ddbe42d553e', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sellorders',
            name='sell_order_token',
            field=models.CharField(default=b'fe384adc-6435-4356-9ca2-b0f146035ccb', max_length=70, primary_key=True, serialize=False),
        ),
    ]
