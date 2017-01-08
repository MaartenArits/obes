/**
 * Created by test-tinkerbox on 18.10.16.
 */

import {NgModule, ErrorHandler} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {HttpModule, JsonpModule} from "@angular/http";
import {MediaSystemComponent} from "./mediaSystem.component";
import { FormsModule }   from '@angular/forms';

@NgModule({
    imports: [BrowserModule,
        HttpModule,
        JsonpModule,
        FormsModule],
    declarations: [MediaSystemComponent],
    bootstrap: [MediaSystemComponent],
})

export class AppModule {
}