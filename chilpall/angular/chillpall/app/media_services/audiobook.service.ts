/**
 * Created by test-tinkerbox on 19.10.16.
 */

import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {Audiobook} from "./media_objects";

@Injectable()
export class AudiobookService{
    private audiobookUrl = 'serverSide/readobject/audiobook.json';

    audiobooks: Audiobook[];

    constructor(public http: Http){}

    initialise(serverUrl: string): any{
        this.audiobooks = [];
        this.http.get(serverUrl + this.audiobookUrl).subscribe(data => this.processAudiobooks(data.text()));

    }


    processAudiobooks(data: string){
        this.audiobooks = [];
        var jsonAudiobookObject = JSON.parse(data);

        for (var audiobookIndex = 0; audiobookIndex < jsonAudiobookObject.length; audiobookIndex++) {
            var audiobookJSON = jsonAudiobookObject[audiobookIndex];
            var audiobook = new Audiobook(
                audiobookJSON.name,
                audiobookJSON.release_date,
                audiobookJSON.owner,
                audiobookJSON.creation_date,
                audiobookJSON.global_id,
                audiobookJSON.language,
                audiobookJSON.explanation,
                audiobookJSON.publisher,
                audiobookJSON.narrator,
                audiobookJSON.author,
                audiobookJSON.book_path,
                audiobookJSON.art_path
            );

            this.audiobooks.push(audiobook);
        }
    }

    getAudiobooks(): Audiobook[]{
        return this.audiobooks;
    }
}
