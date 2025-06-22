import {inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {EventMetadata} from '../domain/event-metadata';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EventProcesserService {
  private readonly httpClient: HttpClient;
  private readonly baseUrl: string;

  constructor() {
    this.httpClient = inject(HttpClient);
    this.baseUrl = environment.EVENT_PROCESSER_URL;
  }

  sendEvent(event: EventMetadata): Observable<void> {
    return this.httpClient.post<void>(this.baseUrl, event);
  }
}
