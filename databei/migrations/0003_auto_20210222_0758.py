# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-22 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databei', '0002_auto_20210219_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_stock_daily',
            name='volume',
            field=models.IntegerField(blank=True),
        ),
    ]
