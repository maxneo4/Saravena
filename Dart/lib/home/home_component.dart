import 'package:angular2/core.dart';
import 'package:angular2_rbi/directives.dart';
import 'package:zonar/services/user.ConfigurationService.dart';
//import 'package:zonar/app_component.dart';
import 'dart:html';

@Component(
    selector: 'my-home',
    templateUrl: 'home.component.html',   
    directives: const [      
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner
  ],providers: const[UserConfigurationService]
  )

class HomeComponent implements OnInit
{
   
  final UserConfigurationService userConfigurationService;

  HomeComponent(this.userConfigurationService);

  @override
  ngOnInit() {    
    userConfigurationService.controller.add('Menu');    
  }
}