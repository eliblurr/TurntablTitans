import { Component } from '@angular/core';
import { SidebarService } from '../services/sidebar/sidebar.service';

@Component({
  selector: 'app-axa-layout',
  templateUrl: './axa-layout.component.html',
  styleUrls: ['./axa-layout.component.css']
})
export class AxaLayoutComponent {
  opens = this.sideBarService.collapseSideBar
  constructor(public sideBarService:SidebarService) { }
}
