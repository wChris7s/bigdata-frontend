import {Component, inject, OnInit} from '@angular/core';
import {EventHadoopService} from '../../services/event-hadoop.service';
import {ChartModule} from 'primeng/chart';
import {HdfsData} from '../../domain/hdfs-data';
import {Chip} from 'primeng/chip';

@Component({
  selector: 'app-hdfs-results',
  templateUrl: './hdfs-results.component.html',
  styleUrl: './hdfs-results.component.css',
  imports: [ChartModule, Chip]
})
export class HdfsResultsComponent implements OnInit {
  protected chartData: any;
  protected chartOptions: any;
  private readonly eventHadoopService: EventHadoopService;
  protected data!: HdfsData;

  constructor() {
    this.eventHadoopService = inject(EventHadoopService);
  }

  ngOnInit(): void {
    this.loadData();
  }

  loadData() {
    return this.eventHadoopService.getHdfsData().subscribe({
      next: (data) => {
        this.data = data;
        this.chartData = {
          labels: ['Likes', 'Historic Downloads'],
          datasets: [
            {
              label: 'Métricas',
              backgroundColor: ['#42A5F5', '#FFA726'],
              data: [data.totalLikes, data.totalHistoricDownloads]
            }
          ]
        };

        this.chartOptions = {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Estadísticas del sistema'
            }
          }
        };
      }
    });
    /*
    this.data = {
      totalLikes: 123,
      totalHistoricDownloads: 2314,
      totalDownloads: 0
    }
    this.chartData = {
      labels: ['Likes', 'Historic Downloads'],
      datasets: [
        {
          label: 'Métricas',
          backgroundColor: ['#42A5F5', '#FFA726'],
          data: [123, 2314]
        }
      ]
    };

    this.chartOptions = {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Estadísticas del sistema'
        }
      }
    };*/
  }
}

