# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

import json, os, shutil

from .media_objects import Media, Movie, Series, Season, SeriesVideos, AudioBook, Album, Music, MediaLibrary, \
    objects_to_json

from .mediaFileCreator import addMovie, searchToAddMovies, addAudiobook, searchToAddAudiobooks, searchToAddMusic, \
    addMusic, createSeriesTree, copySeriesFiles, createSeriesMetaFiles, searchToAddSeries, findSeriesDataToAdd

mediaLibrary = MediaLibrary()
mediaLibraryLocation = '/home/test-tinkerbox/media-data/'
toAddMediaLocation = '/home/test-tinkerbox/to_add_media/'


# Create your views here.

def index(request):
    return render(request, 'index.html')


def AddMusicObject(request):
    if 'data' in request.POST:
        addMusic(request, toAddMediaLocation, mediaLibraryLocation)

    toAddMediaLibrary = searchToAddMusic(toAddMediaLocation)

    return render(request, 'musicAlbumForm.html',
                  {'albums': toAddMediaLibrary.get_music(),
                   'amount_of_albums': len(toAddMediaLibrary.get_music())})


def AddSeriesObject(request):
    if 'data' in request.POST:
        series_to_add = findSeriesDataToAdd(request)

        working_directory = mediaLibraryLocation + 'series/' + series_to_add.get_name() + '/'

        createSeriesTree(series_to_add, working_directory)
        copySeriesFiles(series_to_add, working_directory)
        createSeriesMetaFiles(series_to_add, working_directory)

        if 'delete_original' in request.POST:
            shutil.rmtree(toAddMediaLocation + 'series/' + series_to_add.get_name() + '/')

    toAddMediaLibrary = searchToAddSeries(toAddMediaLocation)

    return render(request, 'seriesForm.html', {'series': toAddMediaLibrary.get_serie(),
                                               'amount_of_series': len(toAddMediaLibrary.get_serie())})


def AddMovieObject(request):
    if 'data' in request.POST:
        addMovie(request, toAddMediaLocation, mediaLibraryLocation)

    toAddMediaLibrary = searchToAddMovies(toAddMediaLocation)

    return render(request, 'movieForm.html',
                  {'movies': toAddMediaLibrary.get_movie(),
                   'amount_of_movies': len(toAddMediaLibrary.get_movie())})


def AddAudiobookObject(request):
    if 'data' in request.POST:
        addAudiobook(request, toAddMediaLocation, mediaLibraryLocation)

    toAddMediaLibrary = searchToAddAudiobooks(toAddMediaLocation)

    return render(request, 'audiobookForm.html',
                  {'audiobooks': toAddMediaLibrary.get_audiobook(),
                   'amount_of_audiobooks': len(toAddMediaLibrary.get_audiobook())})


def ReadMusicObject(request):
    music_array = mediaLibrary.get_music()
    music_json = objects_to_json(music_array)

    return HttpResponse(music_json)


def ReadSeriesObject(request):
    series_array = mediaLibrary.get_serie()
    series_json = objects_to_json(series_array)

    return HttpResponse(series_json)


def ReadMovieObject(request):
    movie_array = mediaLibrary.get_movie()
    movie_json = objects_to_json(movie_array)

    return HttpResponse(movie_json)


def ReadAudiobookObject(request):
    audiobook_array = mediaLibrary.get_audiobook()
    audiobook_json = objects_to_json(audiobook_array)

    return HttpResponse(audiobook_json)


def Filestructure(request):
    
    for dirname, dirnames, filenames in os.walk(mediaLibraryLocation):
        for filename in filenames:
            if filename == 'meta':
                formated_dir = dirname.split('/', len(mediaLibraryLocation.split('/')) - 1)[-1]
                path_list = formated_dir.split('/')

                media_type = path_list[0]

                if media_type == 'movies':
                    with open(os.path.join(dirname, filename), 'r') as metafile:
                        movie = json.load(metafile)
                        newMovie = Movie(movie['name'], movie['year'], movie['owner'], movie['creation_date'],
                                         movie['global_id'], movie['age'], movie['genres'], movie['explanation'],
                                         movie['movie_path'], movie['trailer_path'], movie['art_path'])

                        mediaLibrary.add_movie_object(newMovie)
                if media_type == 'audiobooks':
                    with open(os.path.join(dirname, filename), 'r') as metafile:
                        audiobook = json.load(metafile)
                        newAudiobook = AudioBook(audiobook['name'], audiobook['year'], audiobook['owner'],
                                                 audiobook['creation_date'], audiobook['global_id'],
                                                 audiobook['language'], audiobook['explanation'], audiobook['narrator']
                                                 , audiobook['author'], audiobook['explanation'], audiobook['book_path']
                                                 , audiobook['art_path'])

                        mediaLibrary.add_audiobook_object(newAudiobook)
                if media_type == 'music':
                    with open(os.path.join(dirname, filename), 'r') as metafile:
                        album = json.load(metafile)
                        if 'music' in album:
                            out_album = Album(album['name'], album['year'], album['owner'], album['creation_date'],
                                              album['global_id'], album['artist'], album['record_label'],
                                              album['art_path'],
                                              album['genres'])
                            for songs in album['music'][0]:
                                with open(songs, 'r') as song_metafile:
                                    song = json.load(song_metafile)
                                    out_album.add_music(song['song_name'], song['music_path'], song['number'], song['global_id'])

                            mediaLibrary.add_album_object(out_album)
                if media_type == 'series':
                    with open(os.path.join(dirname, filename), 'r') as metafile:
                        seriesMeta = json.load(metafile)
                        if "seasons" in seriesMeta:
                            out_series = Series(seriesMeta['name'], seriesMeta['year'], seriesMeta['owner'],
                                                seriesMeta['creation_date'], seriesMeta['global_id'],
                                                seriesMeta['explanation'],
                                                seriesMeta['art_path'], seriesMeta['genres'])

                            for seasonMetaFile in seriesMeta['seasons']:
                                with open(seasonMetaFile, 'r') as seasonMetaString:
                                    seasonMeta = json.load(seasonMetaString)
                                    out_season = Season(seasonMeta['name'], seasonMeta['art_path'],
                                                        seasonMeta['explanation'], seasonMeta['season_number'],
                                                        seasonMeta['release_date'], seasonMeta['global_id'])

                                    for episodeMetaFile in seasonMeta['series_videos']:
                                        with open(episodeMetaFile) as episodeMetaString:
                                            episodeMeta = json.load(episodeMetaString)
                                            out_season.add_video(episodeMeta['name'], episodeMeta['art_path'],
                                                                 episodeMeta['explanation'],
                                                                 episodeMeta['video_number'],
                                                                 episodeMeta['video_path'], episodeMeta['release_date'],
                                                                 episodeMeta['global_id'])

                                    out_series.add_season_object(out_season)
                            mediaLibrary.add_serie_object(out_series)

    return HttpResponseRedirect(reverse('serverSide:index'))
