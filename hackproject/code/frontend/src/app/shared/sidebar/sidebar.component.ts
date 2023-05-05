import { Component, OnInit } from '@angular/core';
import { ThemeServiceService } from 'src/app/theming/theme-service.service';
import {SidebarService} from "../services/sidebar/sidebar.service";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit{

  constructor(
    public sidebarService: SidebarService,private themeService:ThemeServiceService
  ) {}
  ngOnInit(){
    this.changeTheme('spotify')
    }


  changeTheme(name:any) {
    this.themeService.setTheme(name);
  }
}
