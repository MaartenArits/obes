/**
 * Created by test-tinkerbox on 17.11.16.
 */


import {Injectable} from "@angular/core";
import {Http, Response, Jsonp, Headers, RequestOptions} from "@angular/http";
import 'rxjs/add/operator/map';


@Injectable()
export class LoggingService{
    constructor(public http: Http, private _jsonp: Jsonp){}

    serverUrl : string;
    session: number;

    initialise(serverUrl: string){
        this.session = Math.floor((Math.random() * 10000) + 1);
        this.serverUrl = serverUrl;
    }

    log(loggingString: string, eventCode: string){
        let body = "JSON_data=" + loggingString + "&eventCode=" + eventCode + "&session=" + this.session;
        let headers = new Headers({ 'Content-Type': 'application/x-www-form-urlencoded' });
        let options = new RequestOptions({ headers: headers });
        this.http.post(this.serverUrl + 'serverSide/log/', body, options).subscribe(data => this.processPostLog(data.text()));
    }

    processPostLog(data: string){
    }
}
