import { Component, OnInit } from '@angular/core';
import { ThemeServiceService } from 'src/app/theming/theme-service.service';
import {SidebarService} from "../services/sidebar/sidebar.service";
import {FileUploadComponent} from "../../features/file-upload/file-upload.component";
import {MatDialog} from "@angular/material/dialog";
import {ChatService} from "../services/chat/chat.service";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit{
  chatId!: string

  constructor(
    public sidebarService: SidebarService,private themeService:ThemeServiceService,
    public chatService: ChatService,
    public dialog: MatDialog,
  ) {}

  ngOnInit(){
    this.changeTheme('spotify')
    }


  changeTheme(name:any) {
    this.themeService.setTheme(name);
  }

  openUploadFileDialog() {
    this.chatService.getChatId().subscribe((res) => {
      localStorage.setItem('chat_id', res.chat_id)
    })
    this.dialog.open(FileUploadComponent, {width: '450px'});
  }
}
