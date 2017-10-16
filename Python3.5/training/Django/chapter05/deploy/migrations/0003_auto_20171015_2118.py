# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_areainfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='area_code',
            field=models.CharField(max_length=50, verbose_name='区号'),
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='area_name',
            field=models.CharField(max_length=50, verbose_name='地区名'),
        ),
    ]
