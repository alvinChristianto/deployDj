# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-19 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_stock_daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(blank=True, max_length=20)),
                ('openp', models.FloatField(blank=True)),
                ('high', models.FloatField(blank=True)),
                ('low', models.FloatField(blank=True)),
                ('close', models.FloatField(blank=True)),
                ('volume', models.CharField(blank=True, max_length=11)),
                ('market_date', models.DateField(blank=True)),
            ],
        ),
    ]
