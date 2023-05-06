import { Component } from '@angular/core';
import {SidebarService} from "../services/sidebar/sidebar.service";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {

  constructor(
    public sidebarService: SidebarService
  ) {}

  isDarkMode: Boolean = false;

  toggleDarkMode(event: any) {
    this.isDarkMode = event.target.checked;
    if (this.isDarkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }

  disabilities: string[] = [
    "Color Blindness", "Dyslexia", "Autism"
  ];
  selectedDisability: string =  "Here";


}
