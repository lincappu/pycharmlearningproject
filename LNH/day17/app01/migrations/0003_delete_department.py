# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
    ]