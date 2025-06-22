import {Component, inject, OnInit} from '@angular/core';
import {UnplashService} from '../../services/unplash.service';
import {ImgMetadata} from '../../domain/img-metadata';
import {Button} from 'primeng/button';
import {Tag} from 'primeng/tag';
import {EventMetadata} from '../../domain/event-metadata';
import {ProgressSpinner} from 'primeng/progressspinner';
import {EventProcesserService} from '../../services/event-processer.service';
import {Toast} from 'primeng/toast';
import {MessageService} from 'primeng/api';

@Component({
  selector: 'app-image-view',
  imports: [
    Button,
    Tag,
    ProgressSpinner,
    Toast
  ],
  templateUrl: './image-view.component.html',
  styleUrl: './image-view.component.css',
  providers: [MessageService]
})
export class ImageViewComponent implements OnInit {
  protected currentImage: ImgMetadata | null;
  protected isLoading: boolean;

  private readonly messageService: MessageService;
  private readonly unplashService: UnplashService;
  private readonly eventProcesserService: EventProcesserService;

  constructor() {
    this.currentImage = null;
    this.isLoading = false;
    this.messageService = inject(MessageService);
    this.unplashService = inject(UnplashService);
    this.eventProcesserService = inject(EventProcesserService);
  }

  ngOnInit(): void {
    this.loadNextImage();
  }

  onLoadDisableLoading() {
    this.isLoading = false;
  }

  rateImage(liked: boolean): void {
    if (sessionStorage.getItem('randomUser') === null || sessionStorage.getItem('randomUser') === undefined) {
      this.messageService.add({
        severity: 'error',
        summary: 'Error',
        detail: "Sesión de usuario no valida. Actualice la página."
      });
      return;
    } else {
      const eventMetadata = {
        username: sessionStorage.getItem('randomUser'),
        like: liked,
        imageDescription: this.currentImage?.alt_description || '',
        historicLikes: this.currentImage?.likes || 0,
        historicDownloads: this.currentImage?.downloads || 0,
        tags: this.currentImage?.tags.map(tag => tag.title) || []
      } as EventMetadata;
      this.eventProcesserService.sendEvent(eventMetadata).subscribe();
      this.loadNextImage();
    }
  }

  private loadNextImage(): void {
    this.isLoading = true;
    this.unplashService.getRandomImage().subscribe((image) => {
      this.currentImage = image;
    });
  }
}
