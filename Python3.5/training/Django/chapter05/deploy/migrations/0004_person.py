# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20171015_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('person_name', models.CharField(max_length=30, verbose_name='名字')),
                ('person_age', models.IntegerField(verbose_name='年龄')),
                ('person_sex', models.CharField(max_length=5, verbose_name='性别')),
                ('person_area', models.ForeignKey(verbose_name='地区', to='deploy.AreaInfo')),
            ],
        ),
    ]
