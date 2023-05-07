import { Component } from '@angular/core';
import { FileUploadService } from '../services/file-upload/file-upload.service';
import {SidebarService} from "../services/sidebar/sidebar.service";
// import { Option } from 'ng-select';

@Component({
  selector: 'app-top-navbar',
  templateUrl: './top-navbar.component.html',
  styleUrls: ['./top-navbar.component.css']
})
export class TopNavbarComponent {
  constructor(
    private sidebarService: SidebarService,
    private fileService: FileUploadService,
  ) {}

  languages: string[] = [];
  selectedItem: string = "ENGLISH";

  ngOnInit(): void {
    this.getLanguages()
  }

  controlSideBar() {
    this.sidebarService.collapseSideBar = !this.sidebarService.collapseSideBar;
  }

  getLanguages(){
    this.fileService.getLanguages().subscribe(
      (res) => this.languages = res.languages
    )
  }
}
