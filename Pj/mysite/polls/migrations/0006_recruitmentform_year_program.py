# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170615_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitmentform',
            name='year_program',
            field=models.CharField(default=4, max_length=200),
            preserve_default=False,
        ),
    ]
