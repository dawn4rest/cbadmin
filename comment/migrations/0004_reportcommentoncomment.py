# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-06 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0003_auto_20190105_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCommentOnComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('report_reason', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('abuse', '심한 욕설을 포함하고 있어요 NO!'), ('infringement', '명예훼손/사생활침해 및 저작권침해!'), ('obscenity', '음란성 또는 청소년에게 매우 유해!'), ('Prosperity', '느닷없는 홍보 게시물 발견!'), ('irrelevant', '의견과 무관한 아무말 대잔치 댓글!')], max_length=50, null=True)),
                ('etc_text', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_on_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.CommentOnComment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
