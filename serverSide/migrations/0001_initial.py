# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-08 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('language', models.CharField(default='ENG', max_length=50)),
                ('sex', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateTimeField(null=True)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('active', models.BooleanField(default=False)),
                ('company', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
