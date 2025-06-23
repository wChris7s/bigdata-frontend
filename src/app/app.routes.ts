import {Routes} from '@angular/router';
import {HomePageComponent} from './pages/home-page/home-page.component';
import {ImageViewComponent} from './components/image-view/image-view.component';
import {HdfsResultsComponent} from './pages/hdfs-results/hdfs-results.component';

export const routes: Routes = [
  {
    path: "home",
    component: HomePageComponent,
    children: [
      {
        path: "view",
        component: ImageViewComponent,
      },
      {
        path: "hdfs",
        component: HdfsResultsComponent,
      }
    ]
  },
  {
    path: "**",
    pathMatch: "full",
    redirectTo: "home"
  }
];
