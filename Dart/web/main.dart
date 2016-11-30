import 'package:angular2/core.dart';
import 'package:angular2/platform/browser.dart';

import 'package:zonar/app_component.dart';
import 'package:http/browser_client.dart';
import 'package:http/http.dart';



void main() {
  bootstrap(AppComponent,  [provide(Client, useFactory: () => new BrowserClient(), deps: [])] );
}
