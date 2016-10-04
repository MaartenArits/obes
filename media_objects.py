import json


class Media(object):
    def __init__(self, name, year, owner, creation_date, global_id):
        self.name = name
        self.year = year
        self.owner = owner
        self.creation_date = creation_date
        self.global_id = global_id

    def get_name(self):
        return self.name

    def get_year(self):
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
        self.group = group

    def get_age(self):
        return self.age

    def get_genres(self):
        return self.year

    def get_explanation(self):
        return self.explenation

    def get_movie_path(self):
        return self.movie_path

    def get_trailer_path(self):
        return self.trailer_path

    def get_art_path(self):
        return self.art_path


class SeriesSeason(Media):
    def __init__(self, name, year, owner, creation_date, global_id, explanation, series_paths, art_path, season_number, genres):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.explanation = explanation
        self.series_paths = series_paths
        self.art_path = art_path
        self.season_number = season_number
        self.genres = genres

    def get_explanation(self):
        return self.explanation

    def get_series_paths(self):
        return self.series_paths

    def get_art_path(self):
        return self.art_path

    def get_season_path(self):
        return self.season_number


class AudioBook(Media):
    def __init__(self, name, year, owner, creation_date, global_id, language, explanation, publisher, narrator, author,
                 book_path, art_path):
        media.__init__(self, name, year, owner, creation_date, global_id)
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


class Album(Media):
    def __init__(self, name, year, owner, creation_date, global_id, artist, record_label, art_path, music_paths,
                 genres):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.artist = artist
        self.record_label = record_label
        self.art_path = art_path
        self.music_paths = music_paths
        self.genres = genres

    def get_artist(self):
        return self.artist

    def get_record_label(self):
        return self.record_label

    def get_art_path(self):
        return self.art_path

    def get_music_path(self):
        return self.music_paths

    def genres(self):
        return self.genres


class Misc(Media):
    def __init__(self, name, year, owner, creation_date, global_id, explanation, document_type, active, location):
        Media.__init__(self, name, year, owner, creation_date, global_id)
        self.explanation = explanation
        self.document_type = document_type
        self.active = active
        self.location = location

    def get_explanation(self):
        return self.explanation

    def get_document_type(self):
        return self.document_type

    def get_active(self):
        return self.active

    def get_location(self):
        return self.location



    def set_active(self, active_status):
        self.active = active_status

    def set_explanation(self, new_explanation):
        self.explanation = new_explanation

    def set_location(self, new_location):
        self.location = new_location