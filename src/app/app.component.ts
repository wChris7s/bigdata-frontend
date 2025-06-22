import {Component, OnInit} from '@angular/core';
import {RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  ngOnInit(): void {
    const existingUser = sessionStorage.getItem('randomUser');
    if (!existingUser) {
      const newUser = this.generateRandomUsername();
      sessionStorage.setItem('randomUser', newUser);
    }
    const currentUser = sessionStorage.getItem('randomUser');
    console.log({"user": currentUser});
  }

  generateRandomUsername(): string {
    const adjectives = ['fast', 'funny', 'bright', 'cool', 'lazy'];
    const animals = ['fox', 'cat', 'panda', 'koala', 'tiger'];
    const randomAdjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const randomAnimal = animals[Math.floor(Math.random() * animals.length)];
    const randomNumber = Math.floor(Math.random() * 1000);
    return `${randomAdjective}-${randomAnimal}-${randomNumber}`;
  }
}
