# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-08 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
