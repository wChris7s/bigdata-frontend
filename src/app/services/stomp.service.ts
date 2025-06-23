import {Injectable} from '@angular/core';
import SockJS from 'sockjs-client';
import {Client} from '@stomp/stompjs';
import {Observable, Subject} from 'rxjs';
import {UserLike} from '../domain/user-like';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class StompService {
  private stompClient!: Client;
  private readonly baseUrl: string;
  private messageSubject: Subject<any> = new Subject();

  constructor() {
    this.baseUrl = environment.EVENT_WS_URL;
    this.connect();
  }

  connect() {
    this.stompClient = new Client({
      webSocketFactory: () => new SockJS(this.baseUrl),
      reconnectDelay: 5000,
      debug: (str) => console.log(str)
    });

    this.stompClient.onConnect = (frame) => {
      console.log('Conectado: ' + frame);
      this.stompClient.subscribe('/topic/likes', message => {
        this.messageSubject.next(JSON.parse(message.body) as UserLike);
      });
    };

    this.stompClient.activate();
  }

  getMessages(): Observable<UserLike> {
    return this.messageSubject.asObservable();
  }
}
