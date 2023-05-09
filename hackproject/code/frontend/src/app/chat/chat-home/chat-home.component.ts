import {Component, ViewChild} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {ChatService} from "../../shared/services/chat/chat.service";
import {MatDialog} from "@angular/material/dialog";
import {FileUploadComponent} from "../../features/file-upload/file-upload.component";
import {SharedService} from "../../shared/services/shared/shared.service";
import {ChatPrompt, ChatRequest} from "../../shared/models/chat";

export interface Message {
  type: string;
  message: string;
}

@Component({
  selector: 'app-chat-home',
  templateUrl: './chat-home.component.html',
  styleUrls: ['./chat-home.component.css']
})
export class ChatHomeComponent {
  currentTheme: any = localStorage.getItem('theme');

  selectedCategory: number = 0;
  fileName = '';
  showButton = false;
  loading = false
  chatForm: FormGroup = this.formBuilder.group({
    body: this.formBuilder.control('', Validators.required),
  })

  constructor(
    private http: HttpClient,
    private formBuilder: FormBuilder,
    private dialog: MatDialog,
    public sharedService: SharedService,
    private chatService: ChatService) {
  }

  sendMessage() {
    this.loading = true;
    // this.scrollToBottom();
    const chatId = this.sharedService.chatId
    const chatMessage = this.chatForm.get('body')?.value
    const chatPrompt: ChatPrompt = {body: chatMessage, native_language: this.sharedService.nativeLanguage}
    const request: ChatRequest = {prompt: chatPrompt, chat_id: chatId}
    this.chatForm.reset()
    const newMessage = this.sharedService.createMessage('user', chatMessage);
    this.sharedService.addMessage(chatId, newMessage)
    this.sharedService.loading = true
    this.chatService.sendMessage(request).subscribe((res) => {
      this.sharedService.addMessage(chatId, {type: 'client', message: res.response})
      this.sharedService.loading = false
    })

  }

  openUploadFileDialog() {
    this.dialog.open(FileUploadComponent, {width: '450px'});
  }

  updateButtonVisibility() {
    this.showButton = this.chatForm.get('body')?.value.trim().length > 0;
  }

  textToSpeech(text: string) {
    this.sharedService.textToSpeech(text, "en")
  }
}
