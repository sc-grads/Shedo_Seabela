import { AppComponent } from './app.component';
import { Component } from '@angular/core';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomePage } from './Pages/HomePage/HomePage.component'
import { RegistrationPage } from './Pages/RegistrationPage/RegistrationPage.component'

const routes: Routes = [
  { path: '', component: HomePage },
  { path: 'RegistrationPage', component: RegistrationPage ,},
 ];

@NgModule({
  declarations: [
    AppComponent,
    HomePage,
    RegistrationPage
         ],
  imports: [
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppModule {

}
