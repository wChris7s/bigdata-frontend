import { Component } from '@angular/core';
import {ImageViewComponent} from '../../components/image-view/image-view.component';
import {NavbarComponent} from '../../components/navbar/navbar.component';

@Component({
  selector: 'app-home-page',
  imports: [
    ImageViewComponent,
    NavbarComponent
  ],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent {

}
