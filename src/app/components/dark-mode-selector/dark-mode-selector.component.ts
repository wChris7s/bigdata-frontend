import {Component} from '@angular/core';
import {Button} from 'primeng/button';

@Component({
  selector: 'app-dark-mode-selector',
  imports: [
    Button
  ],
  templateUrl: './dark-mode-selector.component.html',
  styleUrl: './dark-mode-selector.component.css'
})
export class DarkModeSelectorComponent {
  toggleDarkMode() {
    const element = document.querySelector('html');
    element?.classList.toggle('app-dark');
  }
}
