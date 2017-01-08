/**
 * Created by tinkerbox on 19.11.16.
 */

import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {infoBoxObject} from "./infoBoxObject";

@Injectable()
export class InfoBoxService {
    private infoboxUrl = 'serverSide/readInfoBox/';

    infoboxArray: infoBoxObject[];

    constructor(public http: Http) {
    }

    initialise(serverUrl: string): any {
        this.infoboxArray = [];
        this.http.get(serverUrl + this.infoboxUrl).subscribe(data => this.processInfobox(data.text()));

    }

    processInfobox(data: string) {
        this.infoboxArray = [];
        var jsonInfoBoxObject = JSON.parse(data);

        for (var infoboxIndex = 0; infoboxIndex < jsonInfoBoxObject.length; infoboxIndex++) {
            var infoboxJSON = jsonInfoBoxObject[infoboxIndex];
            var infobox = new infoBoxObject();
            infobox.name = infoboxJSON.name;
            infobox.explanation = infoboxJSON.description;
            infobox.moreInfo = infoboxJSON.moreInfo;
            infobox.visible = infoboxJSON.visible;
            if(infoboxJSON.feedbackFormName){
                infobox.feedbackName = infoboxJSON.feedbackFormName;
            } else {
                infobox.feedbackName = '';
            }
            infobox.art_path = infoboxJSON.art_path;

            this.infoboxArray.push(infobox);
        }
    }

    getInfobox(): infoBoxObject[] {
        return this.infoboxArray;
    }
}

