# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-05 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Body_comment',
            field=models.CharField(max_length=2000),
        ),
    ]
