# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description',
            field=models.TextField(default=b''),
        ),
    ]