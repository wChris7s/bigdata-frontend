import {Component, inject, OnInit} from '@angular/core';
import {UnplashService} from '../../services/unplash.service';
import {ImgMetadata} from '../../domain/img-metadata';
import {Button} from 'primeng/button';
import {Tag} from 'primeng/tag';
import {EventMetadata} from '../../domain/event-metadata';
import {ProgressSpinner} from 'primeng/progressspinner';

@Component({
  selector: 'app-image-view',
  imports: [
    Button,
    Tag,
    ProgressSpinner
  ],
  templateUrl: './image-view.component.html',
  styleUrl: './image-view.component.css'
})
export class ImageViewComponent implements OnInit {
  protected currentImage: ImgMetadata | null;
  protected isLoading: boolean;
  private readonly unplashService: UnplashService;


  constructor() {
    this.currentImage = null;
    this.isLoading = false;
    this.unplashService = inject(UnplashService);
  }

  ngOnInit(): void {
    this.loadNextImage();
  }

  onLoadDisableLoading() {
    this.isLoading = false;
  }

  rateImage(liked: boolean): void {
    console.log(liked ? 'Like' : 'Dislike', this.currentImage);
    const eventMetadata = {
      username: sessionStorage.getItem('randomUser'),
      like: liked,
      imageDescription: this.currentImage?.alt_description || '',
      historicLikes: this.currentImage?.likes || 0,
      historicDownloads: this.currentImage?.downloads || 0,
      tags: this.currentImage?.tags.map(tag => tag.title) || []
    } as EventMetadata;
    console.log({eventMetadata});
    this.loadNextImage();
  }

  private loadNextImage(): void {
    this.isLoading = true;
    this.unplashService.getRandomImage().subscribe((image) => {
      this.currentImage = image;
    });
  }
}
