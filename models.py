# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime


# create your models here.



# professional grouping
class professional_user(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    logo_file = models.FileField(blank=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)


    # user


class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    call_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    birthday = models.DateField(blank=True)
    sex = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    company = models.BooleanField(default=False)


class user_contact_email(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    email_adress = models.CharField(max_length=2000)


class user_contact_phone(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=2000)


# log
class log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.BigIntegerField(default=0)
    event_code = models.IntegerField(default=0)
    json_data = models.CharField(max_length=20000, default="")  # 20 000
    user_id = models.ForeignKey(user)
