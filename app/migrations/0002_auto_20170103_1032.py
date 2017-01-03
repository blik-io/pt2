# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-03 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='bar',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='device',
            name='hum',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='device',
            name='temp',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]