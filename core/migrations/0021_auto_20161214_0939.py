# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-14 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20161212_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='projects',
            field=models.ManyToManyField(blank=True, to='core.Project'),
        ),
    ]
