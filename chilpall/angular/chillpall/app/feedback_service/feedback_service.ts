/**
 * Created by tinkerbox on 20.11.16.
 */
import {Injectable} from "@angular/core";
import {Http, Response, Jsonp, Headers, RequestOptions} from "@angular/http";
import 'rxjs/add/operator/map';


@Injectable()
export class FeedbackService{
    constructor(public http: Http, private _jsonp: Jsonp){}

    serverUrl : string;

    initialise(serverUrl: string){
        this.serverUrl = serverUrl;
    }

    feedback(name: string, email: string, feedback: string){
        let body = 'name=' + name + '&email=' + email + '&feedback=' + feedback;
        let headers = new Headers({ 'Content-Type': 'application/x-www-form-urlencoded' });
        let options = new RequestOptions({ headers: headers });
        this.http.post(this.serverUrl + 'serverSide/feedback/', body, options).subscribe(data => this.processPostFeedback(data.text()));
    }

    processPostFeedback(data: string){
    }
}