# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goodsbrowse'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('carts_amount', models.IntegerField(default=0)),
                ('carts_goods', models.ForeignKey(to='goods.GoodsInfo')),
                ('carts_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
