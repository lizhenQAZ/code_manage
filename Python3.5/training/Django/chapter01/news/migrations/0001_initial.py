# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('news_title', models.CharField(max_length=50)),
                ('news_content', models.CharField(max_length=5000)),
                ('news_category', models.ForeignKey(to='news.NewsCategory')),
            ],
        ),
    ]
