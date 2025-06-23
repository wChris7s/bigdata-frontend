import {Component, inject, OnInit} from '@angular/core';
import {EventHadoopService} from '../../services/event-hadoop.service';
import {ChartModule} from 'primeng/chart';

@Component({
  selector: 'app-hdfs-results',
  templateUrl: './hdfs-results.component.html',
  styleUrl: './hdfs-results.component.css',
  imports: [ChartModule]
})
export class HdfsResultsComponent implements OnInit {
  protected chartData: any;
  protected chartOptions: any;
  private readonly eventHadoopService: EventHadoopService;

  constructor() {
    this.eventHadoopService = inject(EventHadoopService);
  }

  ngOnInit(): void {
    this.loadData();
  }

  loadData() {
    return this.eventHadoopService.getHdfsData().subscribe({
      next: (data) => {
        this.chartData = {
          labels: ['Likes', 'Downloads', 'Historic Downloads'],
          datasets: [
            {
              label: 'Métricas',
              backgroundColor: ['#42A5F5', '#66BB6A', '#FFA726'],
              data: [data.totalLikes, data.totalDownloads, data.totalHistoricDownloads]
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
  }
}
