# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('place_address', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'my_custom_place',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('gender', models.BooleanField(default=False)),
                ('age', models.IntegerField(default=0)),
                ('activity', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
