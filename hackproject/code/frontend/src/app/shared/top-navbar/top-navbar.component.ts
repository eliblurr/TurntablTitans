import { Component } from '@angular/core';
import {SidebarService} from "../services/sidebar/sidebar.service";

@Component({
  selector: 'app-top-navbar',
  templateUrl: './top-navbar.component.html',
  styleUrls: ['./top-navbar.component.css']
})
export class TopNavbarComponent {
  constructor(
    private sidebarService: SidebarService
  ) {}

  controlSideBar() {
    this.sidebarService.collapseSideBar = !this.sidebarService.collapseSideBar;
  }
}
