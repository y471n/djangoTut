# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_image',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(default=None),
        ),
    ]
