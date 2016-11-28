import 'ProviderR.dart';
import 'dart:async';
import 'package:angular2/core.dart';

final List<Provider> _providersMock = [
    new ProviderR('Carrensa', 0),
    new ProviderR('Globant', 0),
    new ProviderR('TeleRecargas', 1000000),
    new ProviderR('Asexac', 2000000)
  ];

@Injectable()
class ProviderService
{
  
  ProviderService();

  Future<List<ProviderR>> getProviders() async {
    return new Future<List<ProviderR>>.value(_providersMock);
  }
    

}