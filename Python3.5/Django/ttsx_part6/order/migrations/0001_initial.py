# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=50)),
                ('goods_price', models.IntegerField()),
                ('goods_img', models.ImageField(upload_to='')),
                ('goods_num', models.IntegerField()),
                ('goods_unit', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('order_number', models.CharField(max_length=50)),
                ('order_status', models.SmallIntegerField(choices=[(1, '待付款'), (2, '待发货'), (3, '待收货'), (4, '已完成')], default=1)),
                ('order_recv', models.CharField(max_length=20)),
                ('order_addr', models.CharField(max_length=50)),
                ('order_tele', models.CharField(max_length=11)),
                ('order_pay', models.SmallIntegerField(choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝支付'), (4, '银联支付')], default=1)),
                ('order_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='goods_order',
            field=models.ForeignKey(to='order.Order'),
        ),
    ]
