# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, time

from django.db import models


# Create your models here.
class Media_User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    language = models.CharField(default="ENG", max_length=50)
    sex = models.CharField(null=True, max_length=50)
    birthday = models.DateTimeField(null=True)

    creation_timestamp = models.DateTimeField('date created', auto_now_add=True)
    active = models.BooleanField(default=False)
    company = models.CharField(null=True, max_length=100)

    def __str__(self):  # datetime word niet ondersteund door json => helper voor serialisatie
        user = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'language': self.language,
            'sex': self.sex,
            'birthday': str(self.birthday),
            'creation_timestamp': str(self.creation_timestamp),
            'active': self.active,
            'company': self.company,
        }

        return json.dumps(user)


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.BigIntegerField(default=0)
    event_code = models.IntegerField(default=0)
    json_data = models.CharField(max_length=20000, default="")
    media_user_id = models.ForeignKey(Media_User)

    def __str__(self):
        log = {
            'timestamp': str(self.timestamp),
            'session_id': self.session_id,
            'event_code': self.event_code,
            'json_data': self.json_data,
            'media_user_id': str(self.media_user_id),
        }

        return json.dumps(log)


class User_Contact_Email(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    email_adress = models.CharField(max_length=200)
    media_user_id = models.ForeignKey(Media_User)

    def __str__(self):
        contact_email = {
            'creation_date': str(self.creation_date),
            'active': self.active,
            'email_adress': self.email_adress,
            'media_user_id': str(self.media_user_id),
        }

        return json.dumps(contact_email)
