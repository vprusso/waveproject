# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_documententry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='documententry',
            name='employee_address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='documententry',
            name='employee_name',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='documententry',
            name='expense_description',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='documententry',
            name='category',
            field=models.CharField(default=None, max_length=250),
        ),
    ]