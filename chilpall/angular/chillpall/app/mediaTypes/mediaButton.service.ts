/**
 * Created by test-tinkerbox on 23.10.16.
 */
import {Injectable} from "@angular/core";
import {Button} from "./button";
import {BUTTONS} from "./buttons";

@Injectable() export class MediaButtonService{
    getButtons(): Button[] {
        return BUTTONS;
    }
}