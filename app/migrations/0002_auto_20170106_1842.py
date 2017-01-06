# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 18:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='allowed_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]
