import 'dart:async';
import 'package:angular2/angular2.dart';
import 'package:angular2/core.dart';
import 'package:angular2/router.dart';
import 'package:angular2_rbi/directives.dart';

@Component(
    selector: 'my-login',
    templateUrl: 'login.component.html',   
    directives: const [      
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner,
      CORE_DIRECTIVES,
      FORM_DIRECTIVES,
      MaterialTextfield
  ])

class LoginComponent
{
    final Router _router;

    LoginComponent(this._router);

    Future<Null> go() => _router.navigate(['Home']);

}