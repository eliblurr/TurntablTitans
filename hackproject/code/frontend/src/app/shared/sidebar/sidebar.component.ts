import { Component } from '@angular/core';
import {SidebarService} from "../services/sidebar/sidebar.service";
import {FileUploadComponent} from "../../features/file-upload/file-upload.component";
import {MatDialog} from "@angular/material/dialog";
import {ChatService} from "../services/chat/chat.service";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {
  chatId!: string

  constructor(
    public sidebarService: SidebarService,
    public chatService: ChatService,
    public dialog: MatDialog,
  ) {}

  openUploadFileDialog() {
    this.chatService.getChatId().subscribe((res) => {
      localStorage.setItem('chat_id', res.chat_id)
    })
    this.dialog.open(FileUploadComponent, {width: '450px'});
  }
}
