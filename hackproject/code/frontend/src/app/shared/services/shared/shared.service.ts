import {Injectable} from '@angular/core';
import {Chat, Message} from "../../models/chat";
import {SynthesisService} from "../../services/text-speech-synth/synthesis.service"
import {HttpClient} from "@angular/common/http";
import { Observable, catchError, map, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {

  chatId!: string
  loading = false
  messages: Message[] = []
  chats: Chat[] = []
  newFileName!: string
  chatMap: Map<string, Message[]> = new Map<string, Message[]>();

  constructor(private synthesisService: SynthesisService) {
    this.synthesisService = synthesisService
    // this.http = http
    // , private http: HttpClient
  }

  startNewChat() {
    this.clearMessages()
    const newMessage = this.createMessage('user', this.newFileName)
    this.addToChatsList(this.chatId, this.newFileName)
    this.addMessage(this.chatId, newMessage)
    this.loading = true
  }

  addFileUploadResponse(res: any) {
    this.loading = false
    Object.keys(res).forEach((key) => {
      const value = res[key];
      const newMessage = this.createMessage('client', value);
      this.addMessage(this.chatId, newMessage)
    })
  }

  clearMessages() {
    if (this.messages.length !== 0) {
      this.messages = []
    }
  }

  createMessage(profile: string, text: string): Message {
    return {
      type: profile,
      message: text
    }
  }

  // Add a message to the chat with the specified chat ID
  addMessage(chatId: string, message: Message): void {
    this.messages.push(message)
    const chatMessages = this.messages || [];
    this.chatMap.set(chatId, chatMessages);
    this.saveToLocalStorage();
  }

  addToChatsList(chatId: string, chatName: string) {
    const newChat = {chatId: chatId, chatName: chatName}
    this.chats.push(newChat)
    localStorage.setItem('chatsList', JSON.stringify(this.chats))
  }

  // Save the chat data to local storage
  saveToLocalStorage(): void {
    localStorage.setItem('chatData', JSON.stringify([...this.chatMap]));
  }

  // Retrieve the messages for a specific chat ID
  getMessages(chatId: string): Message[] | undefined {
    return this.chatMap.get(chatId);
  }

  // Retrieve chat data from local storage (if available)
  getChatsData() {
    const storedData = localStorage.getItem('chatData');
    if (storedData) {
      this.chatMap = new Map<string, Message[]>(JSON.parse(storedData));
    }
  }

  hashText(text:string){
    var hash = 0, i, chr;
    if (text.length === 0) return hash;
    for (i = 0; i < text.length; i++) {
      chr   = text.charCodeAt(i);
      hash  = ((hash << 5) - hash) + chr;
      hash |= 0; // Convert to 32bit integer     
    }
    const res = hash.toString() 
    return hash>0 ? res :  res.replace("-", "1")
  }

  playAudio(blobUrl:string){
    let audio = new Audio();
    audio.src = blobUrl
    audio.load();
    audio.play();
  }

  async sourceFileExists(url: string){
    var exists = true
    await fetch(url).then(res=> exists=true ).catch(err=> exists=false )
    return exists
  } 

  async textToSpeech(text:string, language:string) {
    const hash = this.hashText(text)
    var blobUrl = localStorage.getItem('audio_blob') || ''

    if (hash==localStorage.getItem('audio_hash') && await this.sourceFileExists(blobUrl)){  
      return this.playAudio(blobUrl);
    }

    return this.synthesisService.fetch_audio({"text":text,"language":language}, hash.toString())
      .subscribe(
        (blob:any)=> {
          var blobUrl = URL.createObjectURL(blob);
          this.playAudio(blobUrl)
          // load blob and hash into memory
          localStorage.setItem('audio_blob', blobUrl)
          localStorage.setItem('audio_hash', hash.toString())
        }
      )
  }

  // speechToText() {
  //   // const storedData = localStorage.getItem('chatData');
  //   // if (storedData) {
  //   //   this.chatMap = new Map<string, Message[]>(JSON.parse(storedData));
  //   // }
  // }

}
