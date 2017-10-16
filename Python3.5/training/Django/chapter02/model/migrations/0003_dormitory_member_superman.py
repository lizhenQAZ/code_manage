# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_newplace_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('dormitoy_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_dormitory', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='model.Dormitory')),
            ],
        ),
        migrations.CreateModel(
            name='Superman',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('gender', models.NullBooleanField(default=False)),
                ('desc', models.CharField(max_length=200, db_column='description')),
                ('message', models.TextField(max_length=1000)),
                ('age', models.IntegerField(default=0)),
                ('height', models.DecimalField(max_digits=5, decimal_places=2)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('profile', models.FileField(blank=True, upload_to='', null=True)),
                ('photo', models.ImageField(blank=True, upload_to='', null=True)),
            ],
        ),
    ]
