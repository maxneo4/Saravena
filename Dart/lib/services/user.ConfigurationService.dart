import 'package:angular2/core.dart';
import 'dart:async';

@Injectable()
class UserConfigurationService
{
   StreamController fetchDoneController = new StreamController.broadcast();

   Stream get fetchDone => fetchDoneController.stream;
}