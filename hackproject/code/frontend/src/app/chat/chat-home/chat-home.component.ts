import {Component, ViewChild} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {ChatService} from "../../shared/services/chat/chat.service";
import {MatDialog} from "@angular/material/dialog";
import {FileUploadComponent} from "../../features/file-upload/file-upload.component";

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
  currentTheme:any = localStorage.getItem('theme');

  selectedCategory: number = 0;
  fileName = '';
  loading = false
  messages: Message[] = [];
  chatForm: FormGroup = this.formBuilder.group({
    message: this.formBuilder.control('', Validators.required),
  })


  @ViewChild('scrollMe') private myScrollContainer: any;

  constructor(
    private http: HttpClient,
    private formBuilder: FormBuilder,
    public dialog: MatDialog,
    private chatService: ChatService) {
    this.messages.push(
      {
        type: 'client',
        message: 'Hi, how can I help?'
      },
      {
        type: 'user',
        message: 'I need help'
      },
      {
        type: 'client',
        message: 'I am here to help'
      },
      {
        type: 'user',
        message: 'Ouu that is nice'
      },
      {
        type: 'client',
        message: 'Yeahh I know I am cool ;)'
      }
    )
  }

  sendMessage() {
    const sentMessage = this.chatForm.value.message!;
    this.loading = true;
    this.messages.push({
      type: 'user',
      message: sentMessage,
    });
    this.chatForm.reset();
    this.scrollToBottom();
    this.chatService.sendMessage(sentMessage).subscribe((response) => {
      this.loading = false
      this.messages.push({
        type: 'client',
        message: response.message,
      });
      this.scrollToBottom();
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
