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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('news_title', models.CharField(max_length=50)),
                ('news_content', models.TextField()),
                ('new_cag', models.ForeignKey(to='news.NewsCategory')),
            ],
        ),
    ]
