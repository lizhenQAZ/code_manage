# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_auto_20171014_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=20)),
                ('book_read', models.IntegerField(default=0)),
                ('book_comment', models.IntegerField(default=0)),
                ('book_isdelete', models.BooleanField(default=False)),
            ],
        ),
    ]
