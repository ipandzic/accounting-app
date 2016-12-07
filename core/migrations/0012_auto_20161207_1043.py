# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20161207_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='type1',
            new_name='Transaction_type',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2016, 12, 7, 10, 42, 55, 17545, tzinfo=utc), verbose_name='Invoice date'),
        ),
    ]