# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 19:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161206_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='vat_ammount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2016, 12, 6, 19, 18, 33, 207839), verbose_name='Invoice date'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='settlement_ammount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]