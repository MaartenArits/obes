# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-08 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serverSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.BigIntegerField(default=0)),
                ('event_code', models.IntegerField(default=0)),
                ('json_data', models.CharField(default='', max_length=20000)),
                ('media_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serverSide.Media_User')),
            ],
        ),
    ]