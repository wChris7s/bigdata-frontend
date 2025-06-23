import {Component} from '@angular/core';
import {ImageViewComponent} from '../../components/image-view/image-view.component';
import {NavbarComponent} from '../../components/navbar/navbar.component';
import {RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-home-page',
  imports: [
    ImageViewComponent,
    NavbarComponent,
    RouterOutlet
  ],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent {

}
