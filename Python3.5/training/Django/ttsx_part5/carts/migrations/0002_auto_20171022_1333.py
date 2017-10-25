# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='carts_amount',
            new_name='cart_amount',
        ),
        migrations.RenameField(
            model_name='carts',
            old_name='carts_goods',
            new_name='cart_goods',
        ),
        migrations.RenameField(
            model_name='carts',
            old_name='carts_user',
            new_name='cart_user',
        ),
    ]
