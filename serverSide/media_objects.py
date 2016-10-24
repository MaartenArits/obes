import json


class Media(object):
    def __init__(self, name, year, owner, creation_date, global_id):
        self.name = name
        self.year = str(year)
        self.owner = owner
        self.creation_date = str(creation_date)
        self.global_id = global_id

    def get_name(self):
        return self.name

    def get_date(self):
        return self.year

    def get_owner(self):
        return self.owner

    def get_creation_date(self):
        return self.creation_date

    def get_global_id(self):
        return self.global_id

    def get_json(self):
        return json.dumps(self.__dict__)


class Movie(Media):
    def __init__(self, name, year, owner, creation_date, global_id, age, genres, explanation, movie_path, trailer_path,
                 art_path):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.age = age
        self.genres = genres
        self.explanation = explanation
        self.movie_path = movie_path
        self.trailer_path = trailer_path
        self.art_path = art_path

    def get_age(self):
        return self.age

    def get_genres(self):
        return self.year

    def get_explanation(self):
        return self.explanation

    def get_movie_path(self):
        return self.movie_path

    def get_trailer_path(self):
        return self.trailer_path

    def get_art_path(self):
        return self.art_path

    def get_json(self):
        return json.dumps(self.__dict__)

    def set_by_json(self, **entries):
        self.__dict__.update(entries)


def encode(obj):
    return obj.__dict__


def objects_to_json(obj):
    media_json = []
    for media in obj:
        media_json.append(json.loads(media.get_json()))

    return json.dumps(media_json)


class SeriesVideos(object):
    def __init__(self, name, art_path, explanation, video_number, video_path, release_date, global_id):
        self.name = name
        self.art_path = art_path
        self.explanation = explanation
        self.video_number = video_number
        self.video_path = video_path
        self.release_date = str(release_date)
        self.global_id = global_id

    def get_global_id(self):
        return self.global_id

    def get_name(self):
        return self.name

    def get_art_path(self):
        return self.art_path

    def get_explanation(self):
        return self.explanation

    def get_video_number(self):
        return self.video_number

    def get_video_path(self):
        return self.video_path

    def get_release_date(self):
        return self.release_date

    def get_json(self):
        return json.dumps(self.__dict__, default=encode)


class Season(object):
    def __init__(self, name, art_path, explanation, season_number, release_date, global_id):
        self.name = name
        self.art_path = art_path
        self.explanation = explanation
        self.season_number = season_number
        self.release_date = str(release_date)
        self.series_videos = []
        self.global_id = global_id

    def get_global_id(self):
        return self.global_id

    def get_name(self):
        return self.name

    def get_art_path(self):
        return self.art_path

    def get_explanation(self):
        return self.explanation

    def get_season_number(self):
        return self.season_number

    def get_videos(self):
        return self.series_videos

    def add_video(self, name, art_path, explanation, video_number, video_path, release_date, global_id):
        self.series_videos = self.series_videos + [
            SeriesVideos(name, art_path, explanation, video_number, video_path, release_date, global_id)]

    def add_video_object(self, video_object):
        self.series_videos = self.series_videos + [video_object]

    def get_release_date(self):
        return self.release_date

    def get_json(self):
        return json.dumps(self.__dict__, default=encode)


class Series(Media):
    def __init__(self, name, year, owner, creation_date, global_id, explanation, art_path, genres):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.explanation = explanation
        self.art_path = art_path
        self.genres = genres
        self.seasons = []

    def get_explanation(self):
        return self.explanation

    def get_art_path(self):
        return self.art_path

    def add_season(self, name, art_path, explanation, season_number, release_date, global_id):
        self.seasons = self.seasons + [Season(name, art_path, explanation, season_number, release_date, global_id)]

    def add_season_object(self, season_object):
        self.seasons = self.seasons + [season_object]

    def get_seasons(self):
        return self.seasons

    def get_genres(self):
        return self.genres

    def get_json(self):
        return json.dumps(self.__dict__, default=encode)


class AudioBook(Media):
    def __init__(self, name, year, owner, creation_date, global_id, language, explanation, publisher, narrator, author,
                 book_path, art_path):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.language = language
        self.explanation = explanation
        self.publisher = publisher
        self.narrator = narrator
        self.author = author
        self.book_path = book_path
        self.art_path = art_path

    def get_language(self):
        return self.language

    def get_explanation(self):
        return self.explanation

    def get_publisher(self):
        return self.publisher

    def get_narrator(self):
        return self.narrator

    def get_author(self):
        return self.author

    def get_book_path(self):
        return self.book_path

    def get_art_path(self):
        return self.art_path

    def get_json(self):
        return json.dumps(self.__dict__)


class Music(object):
    def __init__(self, song_name, music_path, number, global_id):
        self.song_name = song_name
        self.music_path = music_path
        self.number = number
        self.global_id = global_id

    def get_song_name(self):
        return self.song_name

    def get_music_path(self):
        return self.music_path

    def get_number(self):
        return self.number

    def get_global_id(self):
        return self.global_id

    def get_json(self):
        return json.dumps(self.__dict__)


class Album(Media):
    def __init__(self, name, year, owner, creation_date, global_id, artist, record_label, art_path, genres):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.artist = artist
        self.record_label = record_label
        self.art_path = art_path
        self.genres = genres
        self.music = []

    def get_artist(self):
        return self.artist

    def get_record_label(self):
        return self.record_label

    def get_art_path(self):
        return self.art_path

    def get_genres(self):
        return self.genres

    def get_music(self):
        return self.music

    def add_music(self, song_name, music_path, number, global_id):
        self.music = self.music + [Music(song_name, music_path, number, global_id)]

    def add_music_object(self, music_object):
        self.music = self.music + [music_object]

    def get_json(self):
        return json.dumps(self.__dict__, default=encode)


class MediaLibrary(object):
    def __init__(self):
        self.movie_library = []
        self.music_library = []
        self.serie_library = []
        self.audiobook_library = []

    def add_movie(self, name, year, owner, creation_date, global_id, age, genres, explanation, movie_path, trailer_path,
                  art_path):
        self.movie_library = self.movie_library + [Movie(name, year, owner, creation_date, global_id, age, genres,
                                                         explanation, movie_path, trailer_path, art_path)]

    def add_movie_object(self, movie_object):
        if isinstance(movie_object, Movie):
            self.movie_library = self.movie_library + [movie_object]

    def add_serie(self, name, art_path, explanation, video_number, video_path, release_date, genres):
        self.serie_library = self.serie_library + [Series(name, art_path, explanation, video_number, video_path,
                                                          release_date, art_path, genres)]

    def add_serie_object(self, serie_object):
        if isinstance(serie_object, Series):
            self.serie_library = self.serie_library + [serie_object]

    def add_album(self, name, year, owner, creation_date, global_id, artist, record_label, art_path, genres):
        self.music_library = self.music_library + [Album(name, year, owner, creation_date, global_id, artist,
                                                         record_label, art_path, genres)]

    def add_album_object(self, album_object):
        if isinstance(album_object, Album):
            self.music_library = self.music_library + [album_object]

    def add_audiobook(self, name, year, owner, creation_date, global_id, language, explanation, publisher, narrator,
                      author, book_path, art_path):
        self.audiobook_library = self.audiobook_library + [AudioBook(name, year, owner, creation_date, global_id,
                                                                     language, explanation, publisher, narrator,
                                                                     author, book_path, art_path)]

    def add_audiobook_object(self, audiobook_object):
        if isinstance(audiobook_object, AudioBook):
            self.audiobook_library = self.audiobook_library + [audiobook_object]

    def get_movie(self):
        return self.movie_library

    def get_serie(self):
        return self.serie_library

    def get_music(self):
        return self.music_library

    def get_audiobook(self):
        return self.audiobook_library

    def get_json(self):
        return json.dumps(self.__dict__)
