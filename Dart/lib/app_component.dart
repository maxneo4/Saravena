import 'Payes/pay_component.dart';
import 'home/home_component.dart';
import 'login/login_component.dart';
import 'package:angular2/core.dart';
import 'package:angular2_rbi/directives.dart';

import 'package:angular2/router.dart';
import 'providers/provider_component.dart';
import 'reports/report_component.dart';
import 'services/user.ConfigurationService.dart';
import 'updates/update_component.dart';

@Component(
    selector: 'my-app',
    templateUrl: 'app.component.html',
    directives: const [  
      
      ROUTER_DIRECTIVES,
      MaterialButton,
      MaterialMenu,
      MaterialLayout,      
      MaterialSpinner  
    ],
    providers: const[ROUTER_PROVIDERS, UserConfigurationService]
    )

@RouteConfig(const [  
    const Route(
    path: '/update/', 
    name: 'Update', 
    component: UpdateComponent,
    useAsDefault: false
    ),
    const Route(
    path: '/provider/', 
    name: 'Provider', 
    component: ProviderComponent,
    useAsDefault: false
    ),
    const Route(
    path: '/reports/', 
    name: 'Reports', 
    component: ReportComponent,
    useAsDefault: false
    ),
    const Route(
    path: '/pay/', 
    name: 'Pay', 
    component: PayComponent,
    useAsDefault: false
    ),
    const Route(
    path: '/home/', 
    name: 'Home', 
    component: HomeComponent,
    useAsDefault: false
    ),
    const Route(
    path: '/login/', 
    name: 'Login', 
    component: LoginComponent,
    useAsDefault: true
    )
])

class AppComponent implements OnInit
{
     String title = '...';
     bool showMenu = false;

     final UserConfigurationService userConfigurationService;

     AppComponent(this.userConfigurationService)
     {       
       
     }

     handle(String s)
     {
       title = s;
       showMenu = true;
     }
     //http://stackoverflow.com/questions/15717681/dart-how-to-create-listen-and-emits-custom-event
  @override
  ngOnInit() {
        userConfigurationService.fetchDone.listen((String s)=> handle(s));
  }
}