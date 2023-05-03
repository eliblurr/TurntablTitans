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

}
