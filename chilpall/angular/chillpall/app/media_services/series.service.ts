/**
 * Created by test-tinkerbox on 19.10.16.
 */

import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {Series, Season, SeriesVideo} from "./media_objects";

@Injectable()
export class SeriesService{
    private seriesUrl = 'serverSide/readobject/series.json';

    series: Series[];
    constructor(public http: Http){}

    initialise(serverUrl: string) {
        this.series = [];
        this.http.get(serverUrl + this.seriesUrl).subscribe(data => this.processSeries(data.text()));
    }

    processSeries(data: string): any{
        this.series = [];
        var jsonSeriesObject = JSON.parse(data);
        for (var seriesIndex = 0; seriesIndex < jsonSeriesObject.length; seriesIndex++) {
            var seriesJSON = jsonSeriesObject[seriesIndex];
            var series = this.seriesFactory(seriesJSON);

            for (var seasonIndex = 0; seasonIndex < seriesJSON.seasons.length; seasonIndex++) {
                var seasonJSON = seriesJSON.seasons[seasonIndex];
                var season = this.seriesSeasonFactory(seasonJSON);

                for (var videoIndex = 0; videoIndex < seasonJSON.series_videos.length; videoIndex++) {
                    var videoJSON = seasonJSON.series_videos[videoIndex];
                    var video = this.seriesVideoFactory(videoJSON);
                    season.add_video(video);
                }
                series.add_season(season);
            }
            this.series.push(series);
        }
    }

    getSeries(): Series[]{
        return this.series;
    }

    private seriesFactory(seriesJSON: any) {
        return new Series(
            seriesJSON.name,
            seriesJSON.year,
            seriesJSON.owner,
            seriesJSON.creation_date,
            seriesJSON.global_id,
            seriesJSON.explanation,
            seriesJSON.art_path,
            seriesJSON.genres
        );
    }

    private seriesSeasonFactory(seasonJSON: any) {
        return new Season(
            seasonJSON.name,
            seasonJSON.year,
            seasonJSON.owner,
            seasonJSON.creation_date,
            seasonJSON.global_id,
            seasonJSON.explanation,
            seasonJSON.art_path,
            seasonJSON.season_number
        );
    }

    private seriesVideoFactory(videoJSON: any) {
        return new SeriesVideo(
            videoJSON.name,
            videoJSON.year,
            videoJSON.owner,
            videoJSON.creation_date,
            videoJSON.global_id,
            videoJSON.explanation,
            videoJSON.art_path,
            videoJSON.video_number,
            videoJSON.video_path
        );
    }
}
