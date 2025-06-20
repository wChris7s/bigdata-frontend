import {inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {map, Observable, tap} from 'rxjs';
import {ImgMetadata} from '../domain/img-metadata';

@Injectable({
  providedIn: 'root'
})
export class UnplashService {
  private httpClient: HttpClient;
  private readonly baseUrl: string = 'https://api.unsplash.com';
  private readonly CLIENT_ID: string = 'ey1Bw1i_x902LvrF8sydDsD6ePFuMrzZCEgIniv3h7g';

  constructor() {
    this.httpClient = inject(HttpClient);
  }

  getRandomImage(): Observable<ImgMetadata> {
    return this.httpClient.get<Object>(`${this.baseUrl}/photos/random?client_id=${this.CLIENT_ID}`)
      .pipe(
        tap(value => console.log(value)),
        map(value => value as ImgMetadata)
      );
  }
}
