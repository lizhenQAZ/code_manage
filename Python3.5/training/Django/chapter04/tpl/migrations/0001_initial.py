# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('mess_username', models.CharField(max_length=30)),
                ('mess_content', models.CharField(max_length=1000)),
                ('mess_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
