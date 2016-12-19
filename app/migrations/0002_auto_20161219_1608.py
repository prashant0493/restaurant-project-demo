# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='Feedback',
            field=models.TextField(default=None),
        ),
    ]
