import { Component } from '@angular/core';
import {SidebarService} from "../services/sidebar/sidebar.service";

@Component({
  selector: 'app-main-layout',
  templateUrl: './main-layout.component.html',
  styleUrls: ['./main-layout.component.css']
})
export class MainLayoutComponent {
  opens = this.sideBarService.collapseSideBar
  constructor(public sideBarService:SidebarService) { }
}
