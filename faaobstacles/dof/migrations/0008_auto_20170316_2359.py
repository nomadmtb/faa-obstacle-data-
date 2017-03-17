# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 23:59
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dof', '0007_auto_20170311_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='airport',
            name='long',
        ),
        migrations.RemoveField(
            model_name='obstacle',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='obstacle',
            name='long',
        ),
        migrations.AddField(
            model_name='airport',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='obstacle',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
