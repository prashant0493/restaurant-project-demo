# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161219_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='FoodItem',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='Price',
            field=models.CharField(max_length=50),
        ),
    ]
