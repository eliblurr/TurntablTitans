import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import {ThemeServiceService} from 'src/app/theming/theme-service.service';
import {SidebarService} from "../services/sidebar/sidebar.service";
import {FileUploadComponent} from "../../features/file-upload/file-upload.component";
import {MatDialog} from "@angular/material/dialog";
import {ChatService} from "../services/chat/chat.service";
import {SynthesisService} from "../services/text-speech-synth/synthesis.service"
import {SharedService} from "../services/shared/shared.service";
import {Chat} from "../models/chat";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit, AfterViewInit {
  chatId!: string
  selectedChatIndex: number = 0;

  @ViewChild('firstChat') firstChat: any;

  constructor(
    public sidebarService: SidebarService,
    private themeService: ThemeServiceService,
    private chatService: ChatService,
    public sharedService: SharedService,
    public synthesisService: SynthesisService,
    public dialog: MatDialog,
  ) {
  }

  isDarkMode: Boolean = false;

  toggleDarkMode(event: any) {
    this.isDarkMode = event.target.checked;
    if (this.isDarkMode) {
      document.body.classList.add('dark-mode');
      localStorage.setItem('ThemeMode', 'true');
      this.themeService.changeThemeToDark('B' + localStorage.getItem('BuilderTheme'));
    } else {
      localStorage.setItem('ThemeMode', 'false');
      document.body.classList.remove('dark-mode');
      this.changeTheme(localStorage.getItem("BuilderTheme"))
    }
  }

  disabilities: string[] = [
    "Default","Color Blindness", "Dyslexia", "Autism"
  ];

  selectedDisability: any = localStorage.getItem("BuilderTheme");

  chats: Chat[] = []

  ngOnInit() {
    if (localStorage.getItem("BuilderTheme") === null) {
      localStorage.setItem('BuilderTheme', 'Default');
      this.selectedDisability = 'Default';
    }
    this.changeTheme(localStorage.getItem("BuilderTheme"))

    this.getChatLists()
    this.initializeChatList()
    if(this.chats.length !== 0){
      this.getChatData(this.chats[0].chatId, 0)
    }
  }

  ngAfterViewInit() {
    setTimeout(() => {
      this.selectedChatIndex = 0;
    });
  }

  changeTheme(name: any) {
    localStorage.setItem('BuilderTheme', name);
    if (localStorage.getItem('ThemeMode') === 'true') {
      this.themeService.changeThemeToDark('B' + localStorage.getItem('BuilderTheme'));
    } else {
      this.themeService.setTheme(name);
    }

  }

  openUploadFileDialog() {
    this.chatService.getChatId().subscribe((res) => {
      localStorage.setItem('chat_id', res.chat_id)
      this.sharedService.chatId = res.chat_id
    })
    this.dialog.open(FileUploadComponent, {width: '450px'});
  }

  textToSpeech(text: string) {
    this.sharedService.textToSpeech(text, "en")
  }

  getChatData(chatId: string, index: number) {
    this.selectedChatIndex = index;
    this.sharedService.chatId = chatId
    const messages = this.sharedService.getMessages(chatId)
    const fileResponse = this.sharedService.getFileResponse(chatId)
    if (messages == undefined) return
    this.sharedService.fileResponse = fileResponse
    this.sharedService.messages = messages
  }

  getChatLists(): Chat[] {
    this.sharedService.$chats.subscribe(
      (res) => {
        this.chats = res.reverse()
      }
    )
    return []
  }

  // speechToText(){
  //   // this.sharedService.speechToText()
  // }


  initializeChatList() {
    if (this.sharedService.getChatsListFromLocalStorage().length !== 0) {
      this.chats = this.sharedService.getChatsListFromLocalStorage()
    }
  }
}
