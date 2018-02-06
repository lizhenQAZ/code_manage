# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('person_name', models.CharField(verbose_name='名字', max_length=30)),
                ('person_age', models.IntegerField(verbose_name='年龄')),
                ('person_sex', models.CharField(verbose_name='性别', max_length=5)),
                ('person_area', models.ForeignKey(verbose_name='地区', to='deploy.AreaInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
