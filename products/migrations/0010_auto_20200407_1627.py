# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-07 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200401_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-published_date']},
        ),
    ]
