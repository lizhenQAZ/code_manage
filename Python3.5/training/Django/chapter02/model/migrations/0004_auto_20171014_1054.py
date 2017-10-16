# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_dormitory_member_superman'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dormitory',
            old_name='dormitoy_name',
            new_name='dormitory_name',
        ),
    ]
