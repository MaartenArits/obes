# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

import json

from .models import Log, User_Contact_Email, Media_User

from .media_objects import Media, Movie, Series, Season, SeriesVideos, AudioBook, Album, Music, MediaLibrary

mediaLibrary = MediaLibrary()


# Create your views here.

def index(request):
    return render(request, 'index.html')


def AddMusicObject(request):
    if 'data' in request.POST:
        name = request.POST['name']
        year = request.POST['year']
        owner = request.POST['owner']
        global_id = request.POST['global_id']
        artist = request.POST['artist']
        record_label = request.POST['record_label']
        art_path = request.POST['art_path']
        genres = request.POST['genres']
        creation_date = timezone.now()

        song_name = request.POST['song_name']
        music_path = request.POST['music_path']

        temp_album = Album(name, year, owner, creation_date, global_id, artist, record_label, art_path, genres)
        temp_album.add_music_object(Music(song_name, music_path))

        mediaLibrary.add_album_object(temp_album)
        return HttpResponseRedirect(reverse('serverSide:index'))
    else:
        return render(request, 'musicAlbumForm.html')


def AddSeriesObject(request):
    if 'data' in request.POST:
        series_name = request.POST['series_name']
        series_year = request.POST['series_year']
        series_owner = request.POST['series_owner']
        series_global_id = request.POST['series_global_id']
        series_explanation = request.POST['series_explanation']
        series_art_path = request.POST['series_art_path']
        series_genres = request.POST['series_genres']

        season_name = request.POST['season_name']
        season_explanation = request.POST['season_explanation']
        season_number = request.POST['season_number']
        season_date = request.POST['season_date']
        season_art_path = request.POST['season_art_path']

        video_name = request.POST['video_name']
        video_explanation = request.POST['video_explanation']
        video_number = request.POST['video_number']
        video_date = request.POST['video_date']
        video_art_path = request.POST['video_art_path']
        video_path = request.POST['video_path']

        temp_video = SeriesVideos(video_name, video_art_path, video_explanation, video_number, video_path, video_date)
        temp_season = Season(season_name, season_art_path, season_explanation, season_number, season_date)
        temp_series = Series(series_name, series_year, series_owner, timezone.now(), series_global_id,
                             series_explanation, series_art_path, series_genres)

        temp_season.add_video_object(temp_video)
        temp_series.add_season_object(temp_season)
        mediaLibrary.add_serie_object(temp_series)

        return HttpResponseRedirect(reverse('serverSide:index'))
    else:
        return render(request, 'seriesForm.html')


def AddMovieObject(request):
    if 'data' in request.POST:
        name = request.POST['name']
        year = request.POST['year']
        global_id = request.POST['global_id']
        age = request.POST['age']
        genres = request.POST['genres']
        explanation = request.POST['explanation']
        trailer_path = request.POST['trailer_path']
        art_path = request.POST['art_path']
        movie_path = request.POST['movie_path']
        owner = request.POST['owner']

        mediaLibrary.add_movie(name, year, owner, timezone.now(), global_id, age, genres, explanation, movie_path,
                               trailer_path, art_path)

        return HttpResponseRedirect(reverse('serverSide:index'))
    else:
        return render(request, 'movieForm.html')


def AddAudiobookObject(request):
    if 'data' in request.POST:
        name = request.POST['name']
        year = request.POST['year']
        global_id = request.POST['global_id']
        owner = request.POST['owner']
        language = request.POST['language']
        explanation = request.POST['explanation']
        publisher = request.POST['publisher']
        narrator = request.POST['narrator']
        author = request.POST['author']
        book_path = request.POST['book_path']
        art_path = request.POST['art_path']

        mediaLibrary.add_audiobook(name, year, owner, timezone.now(), global_id, language, explanation, publisher, narrator,
                      author, book_path, art_path)

        return HttpResponseRedirect(reverse('serverSide:index'))
    else:
        return render(request, 'audiobookForm.html')

def ReadMusicObject(request):
    music_array = mediaLibrary.get_music()

    return render(request, 'musicAlbums.html', {'albums': music_array,
                                                'amount_of_albums': len(mediaLibrary.get_music())})


def ReadSeriesObject(request):
    series_array = mediaLibrary.get_serie()

    return render(request, 'series.html', {'series': series_array,
                                           'amount_of_series': len(series_array)})


def ReadMovieObject(request):
    movie_array = mediaLibrary.get_movie()

    return render(request, 'movie.html', {'movies': movie_array,
                                           'amount_of_movies': len(movie_array)})


def ReadAudiobookObject(request):
    audiobook_array = mediaLibrary.get_audiobook()

    return render(request, 'audiobook.html', {'audiobooks': audiobook_array,
                                           'amount_of_audiobooks': len(audiobook_array)})
