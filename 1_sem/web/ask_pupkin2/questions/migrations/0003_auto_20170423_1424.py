# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_questions_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='tag',
            field=models.ManyToManyField(to='questions.Tag'),
        ),
    ]
