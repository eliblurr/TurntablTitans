import {Injectable} from '@angular/core';
import {Chat, Message} from "../../models/chat";



@Injectable({
  providedIn: 'root'
})
export class SharedService {

  chatId!: string
  loading = false
  nativeLanguage: string = 'ENGLISH'
  messages: Message[] = []
  chats: Chat[] = []
  chatMap: Map<string, Message[]> = new Map<string, Message[]>();
  file!: File

  constructor() {
  }

  startNewChat() {
    this.clearMessages()
    const newMessage = this.createMessage('user', this.file.name)
    this.addToChatsList(this.chatId, this.file.name)
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
}
