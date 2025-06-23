import {Component, inject, OnInit} from '@angular/core';
import {Button} from 'primeng/button';
import {Toast} from 'primeng/toast';
import {StompService} from '../../services/stomp.service';
import {MessageService} from 'primeng/api';

@Component({
  selector: 'app-navbar',
  imports: [
    Button,
    Toast
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css',
  providers: [MessageService]
})
export class NavbarComponent implements OnInit {
  username: string = '';
  stompService: StompService;
  messageService: MessageService;

  constructor() {
    this.stompService = inject(StompService);
    this.messageService = inject(MessageService);
  }

  ngOnInit(): void {
    this.username = sessionStorage.getItem('randomUser') || 'usuario';
    this.stompService.getMessages().subscribe({
      next: (value) => {
        this.messageService.add({
          severity: "contrast",
          summary: "Mensaje de la aplicación",
          detail: `El usuario "${value.username}" tiene un total de ${value.totalLikes} likes en la aplicación.`
        })
      }
    });
  }
}
