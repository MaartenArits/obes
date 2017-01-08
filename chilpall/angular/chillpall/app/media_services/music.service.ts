/**
 * Created by test-tinkerbox on 19.10.16.
 */

import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {Album, Song} from "./media_objects";

@Injectable()
export class MusicService{
    private musicUrl = 'serverSide/readobject/music.json';

    constructor(public http: Http){}
    music: Album[];

    initialise(serverUrl: string): any{
        this.music = [];
        this.http.get(serverUrl + this.musicUrl).subscribe(data => this.processMusic(data.text()));
    }


    processMusic(data: string): any{
        this.music = [];
        var jsonObject = JSON.parse(data);
        for (var index = 0; index < jsonObject.length; index++) {
            var currentJSONObject = jsonObject[index];

            var album = new Album(currentJSONObject.name,
                currentJSONObject.year,
                currentJSONObject.owner,
                currentJSONObject.creation_date,
                currentJSONObject.global_id,
                currentJSONObject.artist,
                currentJSONObject.record_label,
                currentJSONObject.art_path,
                currentJSONObject.genres);

            for (var songIndex = 0; songIndex < currentJSONObject.music.length; songIndex++) {
                var currentSong = currentJSONObject.music[songIndex];

                album.add_song(new Song(currentSong.song_name,
                    currentSong.year,
                    currentSong.owner,
                    currentSong.creation_date,
                    currentSong.global_id,
                    currentSong.index_number,
                    currentSong.music_path
                ));
            }
            this.music.push(album);
        }
        return this.music;
    }

    getMusic(){
        return this.music;
    }
}
