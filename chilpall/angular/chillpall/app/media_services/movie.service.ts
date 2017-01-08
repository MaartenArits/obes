/**
 * Created by test-tinkerbox on 19.10.16.
 */

import {Injectable} from "@angular/core";
import {Http, Response, Jsonp} from "@angular/http";
import {Movie} from "./media_objects";
import 'rxjs/add/operator/map';

@Injectable()
export class MovieService{
    private movieUrl = 'serverSide/readobject/movie.json';

    constructor(public http: Http, private _jsonp: Jsonp){}

    initialise(serverUrl: string){
        this.movies = [];
        this.http.get(serverUrl + this.movieUrl).subscribe(data => this.processMovies(data.text()));
    }

    movies: Movie[];

    processMovies(data){
        this.movies = [];
        var jsonObject = JSON.parse(data);
        for (var index = 0; index < jsonObject.length; index++) {
            var currentJSONObject = jsonObject[index];
            this.movies.push(this.movieFactory(currentJSONObject));
        }
    }

    getMovies(): Movie[]{
        return this.movies;
    }

    private movieFactory(currentJSONObject: any): Movie {
        return new Movie(currentJSONObject.name,
            currentJSONObject.year,
            currentJSONObject.owner,
            currentJSONObject.creation_date,
            currentJSONObject.global_id,
            currentJSONObject.age,
            currentJSONObject.genres,
            currentJSONObject.explanation,
            currentJSONObject.trailer_path,
            currentJSONObject.trailer_path,
            currentJSONObject.art_path);
    }
}
