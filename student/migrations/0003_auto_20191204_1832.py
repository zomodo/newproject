# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-04 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20191121_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (1, '通过'), (2, '拒绝')], default=0, verbose_name='状态'),
        ),
    ]