/**
 * Created by test-tinkerbox on 18.10.16.
 */

import {Injectable} from "@angular/core";
import {Button} from "./button";
import {BUTTONS} from "./buttons";

@Injectable() export class ButtonService{
    getButtons(): Button[] {
        return BUTTONS;
    }
}