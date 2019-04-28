# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-28 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainmodels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_token',
            field=models.CharField(default=b'40d66b7a-e6e5-4485-9b90-f1b5c7884873', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchaseorders',
            name='purchase_order_token',
            field=models.CharField(default=b'dee0ebb3-76be-4d7d-aa90-bf908029b5b9', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sellorders',
            name='sell_order_token',
            field=models.CharField(default=b'842271b3-a7c3-40ed-96af-57cb0855560d', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sellorders',
            name='shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplychainmodels.Address'),
        ),
    ]