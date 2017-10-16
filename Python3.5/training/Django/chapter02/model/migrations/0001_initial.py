# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_comment', models.IntegerField(default=0)),
                ('book_read', models.IntegerField(default=0)),
                ('book_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=50)),
                ('hero_sex', models.BooleanField(default=True)),
                ('hero_desc', models.TextField()),
                ('hero_delete', models.BooleanField(default=False)),
                ('hero_book', models.ForeignKey(to='model.BookInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('place_address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('res_name', models.CharField(max_length=100)),
                ('res_place', models.OneToOneField(to='model.Place')),
            ],
        ),
    ]
