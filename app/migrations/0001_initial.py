# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.IntegerField()),
                ('loc', models.CharField(max_length=14)),
                ('temp', models.DecimalField(decimal_places=1, max_digits=4)),
                ('hum', models.DecimalField(decimal_places=1, max_digits=4)),
                ('bar', models.DecimalField(decimal_places=1, max_digits=5)),
                ('lux', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=40, unique=True)),
                ('focus', models.BooleanField(default=False)),
                ('allowed_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Location'),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Device'),
        ),
    ]
