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


class professional_video(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(max_length=100)
    professional_user = models.ForeignKey(professional_user)
    description = models.CharField(max_length=1000)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)


class professional_photo(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    professional_user = models.ForeignKey(professional_user)
    description = models.CharField(max_length=10000)  # 10 000
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    location = models.FileField(blank=True)


class professional_misc_file(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    professional_user = models.ForeignKey(professional_user)
    description = models.CharField(max_length=10000)  # 10 000
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    location = models.FileField(blank=True)



    # user


class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    call_name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True)
    sex = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    creation_timestamp = models.DateTimeField(auto_now_add=True)


class user_contact_information(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    email_adress = models.CharField(max_length=2000)



# log
class log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.BigIntegerField(default=0)
    event_code = models.IntegerField(default=0)
    json_data = models.CharField(max_length=20000, default="")  # 20 000
    user_id = models.ForeignKey(user)


    # media
    # media: music
class music(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=1000)
    global_id = models.BigIntegerField()

class music_group(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=1000)
    year = models.DateField(blank=True)
    music_id = models.ForeignKey(music)

class music_genre(models.Model):
    music_group_id = models.ForeignKey(music_group)
    genre = models.CharField(max_length=100)

class music_history(models.Model):
    user_id = models.ForeignKey(user)
    music_id = models.ForeignKey(music)
    time = models.BigIntegerFieldField(auto_now_add=True)
    # media: video
    # media: video: movie


class video(models.Model):
    name = models.CharField(max_length=200)
    creator = models.CharField(max_length=1000)
    date = models.DateField(blank=True)
    rating = models.FloatField(blank=True)
    minimum_age = models.IntegerField(blank=True)
    global_id = models.BigIntegerField()
    movie_location = models.CharField(max_length=1000)
    trailer_location = models.CharField(max_length=1000)
    art_location = models.CharField(max_length=1000)
    episode = models.IntegerField(blank = True)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length= 100)

class video_group(models.Model):
    name = models.CharField(max_length=200)
    video_id = models.ForeignKey(video, blank=True)
    group_id = models.ForeignKey('self', blank = True)
    description = models.CharField(max_length=1000)


class video_genre(models.Model):
    movie_video_id = models.ForeignKey(video)
    genre = models.CharField(max_length = 200)

class video_view_history(models.Model):
    user_id = models.ForeignKey(user)
    movie_video_id = models.ForeignKey(video)
    creation_date = models.DateField(auto_now_add=True)
    viewed_to = models.BigIntegerField()
    done_viewing = models.BooleanField(default = False)


#media: audiobooks
class audiobook(models.Model):
    book_info = models.CharField(max_length=20000)
    year = models.IntegerField()
    publisher = models.CharField(max_length = 1000)
    narrator = models.CharField(max_length=1000)
    rating = models.FloatField()
    length = models.FloatField()
    art = models.CharField(max_length=2000)
    global_id = models.BigIntegerField()
    language = models.CharField(max_length=10)

class audiobook_group(models.Model):
    group_name = models.CharField(max_length=1000)
    information = models.CharField(max_length=20000)
    audio_book_id = models.ForeignKey(audiobook)
    art = models.CharField(max_length=2000)

