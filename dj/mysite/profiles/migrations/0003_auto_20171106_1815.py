# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]