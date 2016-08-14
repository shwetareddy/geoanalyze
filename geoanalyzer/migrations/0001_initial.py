# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-13 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_time', models.DateTimeField()),
                ('pickup_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('pickup_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('dropoff_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('dropoff_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]