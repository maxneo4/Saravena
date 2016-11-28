import 'package:angular2/core.dart';
import 'package:angular2_rbi/directives.dart';
//import 'package:zonar/app_component.dart';

@Component(
    selector: 'my-home',
    templateUrl: 'home.component.html',   
    directives: const [      
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner
  ])

class HomeComponent implements OnInit
{
   
  @override
  ngOnInit() {
    //app.menuAvaliable = true;
  }
}