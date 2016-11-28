import 'package:angular2/core.dart';
import 'package:angular2_rbi/directives.dart';

@Component(
    selector: 'my-pay',
    templateUrl: 'pay.component.html',   
    directives: const [      
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner
  ])

class PayComponent
{
   
}