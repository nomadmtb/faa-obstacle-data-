# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dof', '0005_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
