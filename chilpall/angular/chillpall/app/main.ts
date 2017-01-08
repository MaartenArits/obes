/**
 * Created by test-tinkerbox on 18.10.16.
 */

import {platformBrowserDynamic} from "@angular/platform-browser-dynamic";
import {AppModule} from "./app.module";

const platform = platformBrowserDynamic();

platform.bootstrapModule(AppModule);