# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-26 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
