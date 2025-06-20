import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-navbar',
  imports: [],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent implements OnInit {
  username: string = '';

  ngOnInit(): void {
    this.username = sessionStorage.getItem('randomUser') || 'usuario';
  }
}
