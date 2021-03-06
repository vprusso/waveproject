# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 02:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('category', models.CharField(default=None, max_length=250)),
                ('employee_name', models.CharField(default=None, max_length=250)),
                ('employee_address', models.CharField(default=None, max_length=250)),
                ('expense_description', models.CharField(default=None, max_length=500)),
                ('pre_tax_amount', models.FloatField(default=None)),
                ('tax_name', models.CharField(default=None, max_length=250)),
                ('tax_amount', models.FloatField(default=None)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Document')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyExpenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('year', models.IntegerField()),
                ('monthly_expenditure', models.FloatField(default=None)),
                ('document', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='upload.Document')),
            ],
        ),
    ]
