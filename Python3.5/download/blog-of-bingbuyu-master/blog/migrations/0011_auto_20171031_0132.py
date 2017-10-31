# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('cv', 'opencv'), ('nn', 'neural network')], default='cv', max_length=16),
        ),
    ]
