# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dof', '0009_auto_20170319_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='latitude',
            field=models.FloatField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='longitude',
            field=models.FloatField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='obstacle',
            name='latitude',
            field=models.FloatField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='obstacle',
            name='longitude',
            field=models.FloatField(db_index=True, null=True),
        ),
    ]
