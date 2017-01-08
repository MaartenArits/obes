/**
 * Created by test-tinkerbox on 19.10.16.
 */

import {serialize} from "@angular/compiler/src/i18n/serializers/xml_helper";
/**
 * Created by test-tinkerbox on 19.10.16.
 */


export class MediaLibrary {
    movies: Movie[];
    music: Album[];
    audiobooks: Audiobook[];
    series: Series[];

    constructor(){
        this.movies = [];
        this.music = [];
        this.audiobooks = [];
        this.series = [];
    }

    add_movie(movie: Movie) {
        this.movies.push(movie);
    }

    add_movies(movies: Movie[]) {
        for(var movieIndex = 0; movieIndex < movies.length; movieIndex++){
            this.movies.push(movies[movieIndex]);
        }
    }

    get_movies() {
        return this.movies;
    }

    drop_all_movies(){
        this.movies= [];
    }

    add_album(album: Album){
        this.music.push(album)
    }

    add_albums(albums: Album){
        this.music.concat(albums);
    }

    get_albums(){
        return this.music;
    }

    drop_all_albums(){
        this.music = [];
    }

    drop_all_series(){
        this.series = [];
    }

    get_all_series(){
        return this.series;
    }

    add_series(series: Series){
        this.series.push(series);
    }

    add_multiple_series(series: Series[]){
        this.series.concat(series);
    }

    get_all_audiobooks(){
        return this.audiobooks;
    }

    add_audiobook(audiobook: Audiobook){
        this.audiobooks.push(audiobook);
    }

    add_audiobooks(audiobooks: Audiobook[]){
        this.audiobooks.concat(audiobooks);
    }

    drop_all_audiobooks(){
        this.audiobooks = [];
    }
}

export class Media {
    name: string;
    release_date: string;
    owner: string;
    creation_date: string;
    global_id: number;

    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number) {
        this.name = name
        this.release_date = release_date;
        this.owner = owner;
        this.creation_date = creation_date;
        this.global_id = global_id;
    }

    get_name() {
        return this.name;
    }

    get_release_date() {
        return this.release_date;
    }

    get_owner() {
        return this.owner;
    }

    get_creation_date() {
        return this.creation_date;
    }

    get_global_id() {
        return this.global_id;
    }
}

export class Movie extends Media {
    age: number;
    genres: string;
    explanation: string;
    movie_path: string;
    trailer_path: string;
    art_path: string;

    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, age: number, genres: string, explanation: string, movie_path: string, trailer_path: string, art_path: string) {
        super(name, release_date, owner, creation_date, global_id);
        this.age = age;
        this.genres = genres;
        this.explanation = explanation;
        this.movie_path = movie_path;
        this.trailer_path = trailer_path;
        this.art_path = art_path;
    }

    get_age() {
        return this.age;
    }

    get_genres() {
        return this.genres;
    }

    get_explanation() {
        return this.explanation;
    }

    get_movie_path() {
        return this.movie_path;
    }

    get_trailer_path() {
        return this.trailer_path;
    }

    get_art_path() {
        return this.art_path;
    }
}

export class Audiobook extends Media {
    language: string;
    explenation: string;
    publisher: string;
    narrator: string;
    author: string;
    book_path: string;
    art_path: string;
    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, language: string, explanation: string, publisher: string, narrator: string, author: string, book_path: string, art_path: string) {
        super(name, release_date, owner, creation_date, global_id);
        this.language = language;
        this.explenation = explanation;
        this.publisher = publisher;
        this.narrator = narrator;
        this.author = author;
        this.book_path = book_path;
        this.art_path = art_path;
    }

    get_language(){
        return this.language;
    }

    get_explanation(){
        return this.explenation;
    }

    get_publisher(){
        return this.publisher;
    }

    get_narrator(){
        return this.narrator;
    }

    get_author(){
        return this.author;
    }

    get_book_path(){
        return this.book_path;
    }

    get_art_path(){
        return this.art_path;
    }
}

export class Album extends Media {
    artist: string;
    record_label: string;
    art_path: string;
    genres: string;
    songs: Song[];

    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, artist: string, record_label: string, art_path: string, genres: string){
        super(name, release_date, owner, creation_date, global_id);
        this.artist = artist;
        this.record_label = record_label;
        this.art_path = art_path;
        this.genres = genres;
        this.songs = [];
    }

    add_song(song: Song){
        this.songs.push(song);
    }

    add_songs(songs: Song[]){
        this.songs.concat(songs);
    }

    get_artist(){
        return this.artist;
    }

    get_record_label(){
        return this.record_label;
    }

    get_art_path(){
        return this.art_path;
    }

    get_genres(){
        return this.genres;
    }

    get_songs(){
        return this.songs;
    }
}

export class Song extends Media {
    index_number: number;
    music_path: string;

    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, index_number: number, music_path: string) {
        super(name, release_date, owner, creation_date, global_id);
        this.index_number = index_number;
        this.music_path = music_path;
    }

    get_index_number(){
        return this.index_number;
    }

    get_music_path(){
        return this.music_path;
    }
}

export class Series extends Media {
    explanation: string;
    art_path: string;
    genres: string[];
    seasons: Season[];
    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, explanation: string, art_path: string, genres: string[]) {
        super(name, release_date, owner, creation_date, global_id);
        this.explanation = explanation;
        this.art_path = art_path;
        this.genres = genres;
        this.seasons = [];
    }

    add_season(season: Season){
        this.seasons.push(season);
    }

    add_seasons(seasons: Season[]){
        this.seasons.concat(seasons);
    }

    get_explanation(){
        return this.explanation;
    }

    get_art_path(){
        return this.art_path;
    }

    get_genres(){
        return this.genres;
    }

    get_seasons(){
        return this.seasons;
    }
}

export class Season extends Media {
    art_path: string;
    explanation: string;
    season_number: number;
    series_videos: SeriesVideo[];
    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, explanation: string, art_path: string, season_number: number) {
        super(name, release_date, owner, creation_date, global_id);
        this.explanation = explanation;
        this.art_path = art_path;
        this.season_number = season_number;
        this.series_videos = [];
    }

    add_video(video: SeriesVideo){
        this.series_videos.push(video);
    }

    add_videos(videos: SeriesVideo[]){
        this.series_videos.concat(videos);
    }

    get_explanation(){
        return this.explanation;
    }
    get_art_path(){
        return this.art_path;
    }
    get_season_number(){
        return this.season_number;
    }
    get_series_videos(){
        return this.series_videos;
    }
}

export class SeriesVideo extends Media {
    art_path: string;
    explanation: string;
    video_number: number;
    video_path: string;
    global_id: number;
    constructor(name: string, release_date: string, owner: string, creation_date: string, global_id: number, explanation: string, art_path: string, video_number: number, video_path: string) {
        super(name, release_date, owner, creation_date, global_id);
        this.explanation = explanation;
        this.art_path = art_path;
        this.video_number = video_number;
        this.video_path = video_path;
    }

    get_explanation(){
        return this.explanation;
    }

    get_art_path(){
        return this.art_path;
    }

    get_video_number(){
        return this.video_number;
    }

    get_video_path(){
        return this.video_path;
    }

    get_global_id(){
        return this.global_id;
    }
}

