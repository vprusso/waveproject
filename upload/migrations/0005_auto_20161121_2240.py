# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-22 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20161121_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpenditure',
            name='month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
    ]
