# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-01 17:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0005_auto_20180101_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 1, 17, 9, 41, 377779), verbose_name='添加时间'),
        ),
    ]