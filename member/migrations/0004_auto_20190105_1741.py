# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-05 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20190105_0338'),
        ('member', '0003_auto_20190105_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hate_comments',
            field=models.ManyToManyField(blank=True, related_name='hate_comments', to='comment.Comment'),
        ),
        migrations.AddField(
            model_name='user',
            name='like_comments',
            field=models.ManyToManyField(blank=True, related_name='like_comments', to='comment.Comment'),
        ),
    ]
