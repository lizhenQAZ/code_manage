# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_bookdesc'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('area_name', models.CharField(max_length=30)),
                ('area_parent', models.ForeignKey(blank=True, to='model.AreaInfo', null=True)),
            ],
        ),
    ]
