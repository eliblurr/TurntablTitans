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
  loading = false
  chatForm: FormGroup = this.formBuilder.group({
    message: this.formBuilder.control('', Validators.required),
  })


  @ViewChild('scrollMe') private myScrollContainer: any;

  constructor(
    private http: HttpClient,
    private formBuilder: FormBuilder,
    private dialog: MatDialog,
    public sharedService: SharedService,
    private chatService: ChatService) {
  }

  //to do : work on the native language
  sendMessage() {
    this.loading = true;
    this.scrollToBottom();
    const chatId = this.sharedService.chatId
    const chatPrompt: ChatPrompt = {body: this.chatForm.value.get('message'), native_language: 'ENGLISH'}
    const request: ChatRequest = {prompt: chatPrompt, chat_id: chatId}
    this.chatService.sendMessage(request).subscribe((res) => {
      this.chatForm.reset();
      this.sharedService.loading = true
      this.sharedService.addMessage(chatId, {type: 'client', message: res.response})
      this.sharedService.loading = true
    })
  }

  scrollToBottom() {
    setTimeout(() => {
      try {
        this.myScrollContainer.nativeElement.scrollTop =
          this.myScrollContainer.nativeElement.scrollHeight + 500;
      } catch (err) {
      }
    }, 150);
  }

  onFileSelected(event: any) {

    const file: File = event.target.files[0];

    if (file) {

      this.fileName = file.name;

      const formData = new FormData();

      formData.append("thumbnail", file);

      const upload$ = this.http.post("/api/thumbnail-upload", formData);

      upload$.subscribe();
    }
  }

  openUploadFileDialog() {
    this.dialog.open(FileUploadComponent, {width: '450px'});
  }
}
