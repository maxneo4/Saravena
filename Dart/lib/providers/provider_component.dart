import 'ProviderR.dart';
import 'package:angular2/core.dart';
import 'package:angular2_rbi/directives.dart';
import 'provider_service.dart';

@Component(
    selector: 'my-provider',
    templateUrl: 'provider.component.html',   
    directives: const [      
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner
  ], providers: const [ProviderService]    
  )

class ProviderComponent implements OnInit
{
    List<ProviderR> providers;
    ProviderR _currentProvider;
    final ProviderService _service;

    ProviderComponent(this._service);

  @override
  ngOnInit() async {
    providers = await _service.getProviders();
  }

}