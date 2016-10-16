# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

import json, os, shutil

from .media_objects import Media, Movie, Series, Season, SeriesVideos, AudioBook, Album, Music, MediaLibrary

from .mediaFileCreator import addMovie, searchToAddMovies, addAudiobook, searchToAddAudiobooks, searchToAddMusic, \
    addMusic

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
        series_to_add = findDataToAdd(request)

        working_directory = mediaLibraryLocation + 'series/' + series_to_add.get_name() + '/'

        createSeriesTree(series_to_add, working_directory)
        copySeriesFiles(series_to_add, working_directory)
        createSeriesMetaFiles(series_to_add, working_directory)

    toAddMediaLibrary = searchToAddSeries()

    return render(request, 'seriesForm.html', {'series': toAddMediaLibrary.get_serie(),
                                               'amount_of_series': len(toAddMediaLibrary.get_serie())})


def createSeriesMetaFiles(series_to_add, working_directory):
    metaSeriesObject = Series(series_to_add.get_name(), series_to_add.get_year(), series_to_add.get_owner(),
                              series_to_add.get_creation_date(), series_to_add.get_global_id(),
                              series_to_add.get_explanation(), series_to_add.get_art_path(),
                              series_to_add.get_genres())
    for season in series_to_add.get_seasons():
        season_dir = working_directory + "season " + str(season.get_season_number()) + '/'

        metaSeasonObject = Season(season.get_name(), season.get_art_path(), season.get_explanation(),
                                  season.get_season_number(), season.get_release_date())

        for episode in season.get_videos():
            with open(season_dir + episode.get_name() + '/' + 'meta', 'wb+') as outfile:
                outfile.write(episode.get_json())

            metaSeasonObject.add_video_object(season_dir + episode.get_name() + '/' + 'meta')
        metaSeriesObject.add_season_object(season_dir + 'meta')
        with open(season_dir + 'meta', 'wb+') as outfile:
            outfile.write(metaSeasonObject.get_json())
    with open(working_directory + 'meta', 'wb+') as outfile:
        outfile.write(metaSeriesObject.get_json())


def findDataToAdd(request):
    series_name = request.POST['series_name']
    series_year = request.POST['series_year']
    series_owner = request.POST['series_owner']
    series_global_id = request.POST['series_global_id']
    series_explanation = request.POST['series_explanation']
    series_art_path = request.POST['series_art_path']
    series_genres = request.POST['series_genres']
    series_to_add = Series(series_name, series_year, series_owner, timezone.now(), series_global_id,
                           series_explanation, series_art_path, series_genres)
    for season_number in range(0, int(request.POST['amount_of_seasons'])):
        if ("season_enable." + str(season_number)) in request.POST:
            season_to_add = Season(request.POST["season_name." + str(season_number)],
                                   request.POST["season_art_path." + str(season_number)],
                                   request.POST["season_explanation." + str(season_number)],
                                   request.POST["season_number." + str(season_number)],
                                   request.POST["season_date." + str(season_number)])

            for episode_number in range(0, int(request.POST['amount_of_episodes.' + str(season_number)])):
                if ("video_enable." + str(season_number) + '.' + str(episode_number)) in request.POST:
                    season_to_add.add_video(
                        request.POST['video_name.' + str(season_number) + '.' + str(episode_number)],
                        request.POST['video_art_path.' + str(season_number) + '.' + str(episode_number)],
                        request.POST['video_explanation.' + str(season_number) + '.' + str(episode_number)],
                        request.POST['video_number.' + str(season_number) + '.' + str(episode_number)],
                        request.POST['video_path.' + str(season_number) + '.' + str(episode_number)],
                        request.POST['video_date.' + str(season_number) + '.' + str(episode_number)])
        series_to_add.add_season_object(season_to_add)
    return series_to_add


def createSeriesTree(series_to_add, working_directory):
    os.mkdir(working_directory, 0755)
    for season in series_to_add.get_seasons():
        season_dir = working_directory + "season " + str(season.get_season_number()) + '/'

        os.mkdir(season_dir, 0755)
        for episode in season.get_videos():
            os.mkdir(season_dir + episode.get_name() + '/', 0755)


def copySeriesFiles(series_to_add, working_directory):
    for season in series_to_add.get_seasons():
        season_dir = working_directory + "season " + str(season.get_season_number()) + '/'

        for episode in season.get_videos():
            shutil.copy(episode.get_video_path(), season_dir + episode.get_name() + '/')


def searchToAddSeries():
    toAddMediaLibrary = MediaLibrary()
    active_series = ''
    current_series = ''
    active_season = ''
    current_season = ''
    art_location = []
    episode_location = []
    seasons_to_add = []
    season_number = 0
    for dirname, dirnames, filenames in os.walk(toAddMediaLocation + 'series/'):
        for filename in filenames:
            formated_dir = dirname.split('/', len(toAddMediaLocation.split('/')))[-1]
            path_list = formated_dir.split('/')
            current_series = path_list[0]

            current_season = path_list[1:][0]

            if active_season != '' and active_series != '':
                if active_season != current_season:
                    temp_season_to_add = Season(active_season, art_location, '', season_number, '')
                    season_number += 1
                    for number, location in enumerate(episode_location):
                        episode_name = location.split('/')[-1].split('.')[0]
                        temp_season_to_add.add_video_object(SeriesVideos(episode_name, '', '', number, location, ''))

                    seasons_to_add.append(temp_season_to_add)
                    episode_location = []
                    art_location = []

                if active_series != current_series:
                    temp_series_to_add = Series(active_series, '', '', timezone.now(), '', '', '', '')
                    for season in seasons_to_add:
                        temp_series_to_add.add_season_object(season)

                    toAddMediaLibrary.add_serie_object(temp_series_to_add)
                    art_location = []
                    episode_location = []
                    seasons_to_add = []
                    season_number = 0

            active_season = current_season
            active_series = current_series

            file_extention = filename.split('.')[-1]
            if file_extention == 'JPG':
                art_location.append(os.path.join(dirname, filename))

            if file_extention == 'mp4':
                episode_location.append(os.path.join(dirname, filename))
    if active_season != '' and active_series != '':
        if active_season == current_season:
            temp_season_to_add = Season(active_season, art_location, '', season_number, '')
            for number, location in enumerate(episode_location):
                temp_season_to_add.add_video_object(SeriesVideos(filename, '', '', number, location, ''))

            seasons_to_add.append(temp_season_to_add)
        if active_series == current_series:
            temp_series_to_add = Series(active_series, '', '', timezone.now(), '', '', '', '')
            for season in seasons_to_add:
                temp_series_to_add.add_season_object(season)

            toAddMediaLibrary.add_serie_object(temp_series_to_add)

    return toAddMediaLibrary


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
                                    out_album.add_music(song['song_name'], song['music_path'], song['number'])

                            mediaLibrary.add_album_object(out_album)
                if media_type == 'series':
                    with open(os.path.join(dirname, filename), 'r') as metafile:
                        seriesMeta = json.load(metafile)
                        if "seasons" in seriesMeta:
                            out_series = Series(seriesMeta['name'], seriesMeta['year'], seriesMeta['owner'],
                                                seriesMeta['creation_date'], seriesMeta['global_id'], seriesMeta['explanation'],
                                                seriesMeta['art_path'], seriesMeta['genres'])

                            for seasonMetaFile in seriesMeta['seasons']:
                                with open(seasonMetaFile, 'r') as seasonMetaString:
                                    seasonMeta = json.load(seasonMetaString)
                                    out_season = Season(seasonMeta['name'], seasonMeta['art_path'],
                                                        seasonMeta['explanation'], seasonMeta['season_number'],
                                                        seasonMeta['release_date'])

                                    for episodeMetaFile in seasonMeta['series_videos']:
                                        with open(episodeMetaFile) as episodeMetaString:
                                            episodeMeta = json.load(episodeMetaString)
                                            out_season.add_video(episodeMeta['name'], episodeMeta['art_path'],
                                                                 episodeMeta['explanation'], episodeMeta['video_number'],
                                                                 episodeMeta['video_path'], episodeMeta['release_date'])

                                    out_series.add_season_object(out_season)
                            mediaLibrary.add_serie_object(out_series)




    return HttpResponseRedirect(reverse('serverSide:index'))
