import { Component } from '@angular/core';
import {SidebarService} from "../services/sidebar/sidebar.service";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {
  currentTheme:any = localStorage.getItem('theme');

  constructor(
    public sidebarService: SidebarService
  ) {}

  setTheme(newTheme:any){
    localStorage.setItem('theme',newTheme)
    this.currentTheme = localStorage.getItem('theme');
    location.reload()
  }

}
