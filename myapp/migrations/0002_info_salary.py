# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-27 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
