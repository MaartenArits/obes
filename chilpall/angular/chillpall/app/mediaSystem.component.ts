/**
 * Created by test-tinkerbox on 23.10.16.
 */
import {Component, OnInit, ViewChild} from "@angular/core";
import {AudiobookService} from "./media_services/audiobook.service";
import {MusicService} from "./media_services/music.service";
import {SeriesService} from "./media_services/series.service";
import {MovieService} from "./media_services/movie.service";
import {MediaButtonService} from "./mediaTypes/mediaButton.service";
import {Button} from "./mediaTypes/button";
import {MediaLibrary, Movie, Song, Season} from "./media_services/media_objects";
import {LoggingService} from "./logging_service/logging_service";
import {InfoBoxService} from "./infobox_service/infobox_service";
import {FeedbackService} from "./feedback_service/feedback_service";



@Component({
    moduleId: module.id,
    selector: "my-app",
    templateUrl: "normal_view.html",
    styleUrls: ['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'styles/media_style.css',
        'styles/topbar.css',
        'styles/genres.css',
        'styles/modal.css',
        'styles/mediaBox.css'],
    providers: [MediaButtonService,
        MovieService,
        SeriesService,
        MusicService,
        AudiobookService,
        LoggingService,
        InfoBoxService,
        FeedbackService]
})

export class MediaSystemComponent implements OnInit {

    @ViewChild('videoPlayer') videoplayer: any;

    serverUrl = 'http://127.0.0.1:8000/';

    buttons: Button[];
    genres: Button[];

    selectedMediaButton: Button;
    selectedGenreButton: Button;

    evenSelectedObjects: any[];
    unevenSelectedObjects: any[];

    modal_video_path: string;
    modal_audio_path: string;

    selectedObject: any;
    selectedSong: Song;
    selectedSeason: Season;

    videoActive: boolean;
    musicActive: boolean;
    seasonActive: boolean;

    feedbackName: string;
    feedbackEmail: string;
    feedback: string;

    constructor(private mediaButtonService: MediaButtonService,
                private movieService: MovieService,
                private seriesService: SeriesService,
                private audiobookService: AudiobookService,
                private musicService: MusicService,
                private loggingService: LoggingService,
                private infoboxService: InfoBoxService,
                private feedbackService: FeedbackService) {
    }

    getMediaButtons() {
        this.buttons = this.mediaButtonService.getButtons();
    }

    ngOnInit(): any {
        this.selectedObject = new Movie("", "", "", "", 0, 0, "", "", "", "", "");
        this.getMediaButtons();
        this.genres = [];

        this.modal_video_path = "";
        this.modal_audio_path = "";

        this.selectedMediaButton = {name: 'eula'};

        this.selectedSong = new Song("", "", "", "", 0, 0, "");
        this.selectedSeason = new Season("", "", "", "", 0, "", "", 0);

        this.audiobookService.initialise(this.serverUrl);
        this.musicService.initialise(this.serverUrl);
        this.seriesService.initialise(this.serverUrl);
        this.movieService.initialise(this.serverUrl);

        this.infoboxService.initialise(this.serverUrl);
        this.loggingService.initialise(this.serverUrl);
        this.feedbackService.initialise(this.serverUrl);

        this.musicActive = false;
        this.videoActive = false;
        this.seasonActive = false;



    }

    selectMedia(button: Button) {
        this.selectedMediaButton = button;
        this.loggingService.log(JSON.stringify(button), "redirect");
        this.createGenresTab();
        this.evenSelectedObjects = [];
        this.unevenSelectedObjects = [];
        if (button.name == 'Movies' || button.name == 'Series') {
            this.selectGenre({name: "All"});
            this.videoActive = true;
            this.musicActive = false;
        }

        if (button.name == 'Music' || button.name == 'Audiobooks') {
            this.selectGenre({name: "All"});
            this.videoActive = false;
            this.musicActive = true;
        }

        if (button.name == 'Info') {
            this.createInfoPage();
            this.videoActive = false;
            this.musicActive = false;
        }

    }

    createInfoPage() {
        var unfilteredInfoboxes = this.infoboxService.getInfobox();
        var infoboxes = [];
        for(var infoboxIndex = 0; infoboxIndex < unfilteredInfoboxes.length; infoboxIndex++){
            if(unfilteredInfoboxes[infoboxIndex].visible == 'True'){
                infoboxes.push(unfilteredInfoboxes[infoboxIndex]);
            }
        }
        for (var objectIndex = 0; objectIndex < infoboxes.length; objectIndex += 2) {
            this.evenSelectedObjects.push(infoboxes[objectIndex]);
        }
        for (var objectIndex = 1; objectIndex < infoboxes.length; objectIndex += 2) {
            this.unevenSelectedObjects.push(infoboxes[objectIndex]);
        }
    }

    selectGenre(button: Button) {
        if (Button.name != 'Info') {
            this.loggingService.log(JSON.stringify(button), "redirect");
            this.selectedGenreButton = button;
            this.evenSelectedObjects = [];
            this.unevenSelectedObjects = [];
            var objects = [];
            switch (this.selectedMediaButton.name) {
                case 'Movies':
                    objects = this.movieService.getMovies();
                    break;
                case 'Series':
                    objects = this.seriesService.getSeries();
                    break;
                case 'Music':
                    objects = this.musicService.getMusic();
                    break;
                case 'Audiobooks':
                    objects = this.audiobookService.getAudiobooks();
                    break;
                default:
                    console.log("fault in button click");
            }
            if (button.name == "All") {
                for (var objectIndex = 0; objectIndex < objects.length; objectIndex += 2) {
                    this.evenSelectedObjects.push(objects[objectIndex]);
                }
                for (var objectIndex = 1; objectIndex < objects.length; objectIndex += 2) {
                    this.unevenSelectedObjects.push(objects[objectIndex]);

                }
            } else {
                var objectsToView = [];

                for (var objectIndex = 0; objectIndex < objects.length; objectIndex++) {
                    for (var genre_index = 0; genre_index < objects[objectIndex].get_genres().split(',').length; genre_index++) {
                        if (button.name == objects[objectIndex].get_genres().replace(/\s/g, '').split(',')[genre_index]) {
                            objectsToView.push(objects[objectIndex]);
                            break;
                        }
                    }
                }

                for (var objectIndex = 0; objectIndex < objectsToView.length; objectIndex += 2) {
                    this.evenSelectedObjects.push(objectsToView[objectIndex]);
                }
                for (var objectIndex = 1; objectIndex < objectsToView.length; objectIndex += 2) {
                    this.unevenSelectedObjects.push(objectsToView[objectIndex]);
                }
            }
        }
    }

    createGenresTab() {
        this.genres = [];
        if (this.selectedMediaButton.name != 'Info') {
            this.genres.push({name: "All"});
            this.genres.push({name: "Featured"});
            if (this.selectedMediaButton.name != "Audiobook") {
                var objects = [];
                switch (this.selectedMediaButton.name) {
                    case 'Movies':
                        objects = this.movieService.getMovies();
                        break;

                    case 'Series':
                        objects = this.seriesService.getSeries();
                        break;

                    case 'Music':
                        objects = this.musicService.getMusic();
                        break;

                    case 'Audiobooks':
                        objects = this.audiobookService.getAudiobooks();
                        break;

                    default:
                        console.log("fault in button click");
                }
                for (var objectIndex = 0; objectIndex < objects.length; objectIndex++) {
                    var current_genre_to_process = objects[objectIndex].get_genres().replace(/\s/g, '').split(',');

                    for (var current_genre_to_process_index = 0; current_genre_to_process_index < current_genre_to_process.length; current_genre_to_process_index++) {
                        var unique_genre = true;
                        for (var genreIndex = 0; genreIndex < this.genres.length; genreIndex++) {
                            if (this.genres[genreIndex].name == current_genre_to_process[current_genre_to_process_index]) {
                                unique_genre = false;
                                break;
                            }
                        }
                        if (unique_genre == true) {
                            this.genres.push({name: current_genre_to_process[current_genre_to_process_index]});
                        }
                    }
                }
            }
        }
    }

    selectTrailer(mediaObject: any) {
        this.modal_video_path = mediaObject.get_trailer_path();
        this.selectedModalMedia(mediaObject);
        this.videoplayer.nativeAlement.play();
    }

    selectVideo(mediaObject: any) {
        this.modal_video_path = mediaObject.get_movie_path();
        this.selectedModalMedia(mediaObject);
        this.videoplayer.nativeAlement.play();
    }

    selectedModalMedia(mediaObject: any) {
        this.selectedObject = mediaObject;
    }

    selectSong(song: Song) {
        this.selectedSong = song;
        this.modal_audio_path = song.get_music_path();
    }

    selectSeason(season: Season) {
        this.selectedSeason = season;
        this.seasonActive = true;
    }

    selectSeasonOverview() {
        this.seasonActive = false;
    }

    modalCleanup() {
        this.seasonActive = false;
        this.modal_audio_path = "";
        this.modal_video_path = "";
    }

    submitFeedback(){
        this.feedbackService.feedback(this.feedbackName, this.feedbackEmail, this.feedback);
        this.selectedObject = this.getInfobox(this.selectedObject.feedbackName, this.selectedObject);
    }

    getInfobox(feedbackName: string, currentSelectedObject: any){
        console.log(feedbackName);
        var unfilteredInfoboxes = this.infoboxService.getInfobox();
        for(var infoboxIndex = 0; infoboxIndex < unfilteredInfoboxes.length; infoboxIndex++){
            if(unfilteredInfoboxes[infoboxIndex].name == feedbackName){
                console.log(unfilteredInfoboxes[infoboxIndex].name);
                return unfilteredInfoboxes[infoboxIndex];
            }
        }
        console.log("found none");
        return currentSelectedObject;

    }
}
