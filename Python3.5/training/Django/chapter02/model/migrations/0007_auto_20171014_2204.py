# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_areainfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heroinfo',
            options={'ordering': ['id']},
        ),
    ]
