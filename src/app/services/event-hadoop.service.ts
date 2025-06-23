import {inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {HdfsData} from '../domain/hdfs-data';

@Injectable({
  providedIn: 'root'
})
export class EventHadoopService {
  private readonly httpClient: HttpClient;
  private readonly baseUrl: string;

  constructor() {
    this.httpClient = inject(HttpClient);
    this.baseUrl = environment.EVENT_HADOOP_HDFS;
  }

  getHdfsData(): Observable<HdfsData> {
    return this.httpClient.get<HdfsData>(this.baseUrl);
  }
}
