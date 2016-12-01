import 'package:angular2/core.dart';
import 'package:angular2_rbi/directives.dart';

@Component(
    selector: 'my-report',
    templateUrl: 'report.component.html',   
    directives: const [      
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner
  ])

class ReportComponent
{   
}