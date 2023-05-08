import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {ChatId} from "../../models/chatId";
import {environment} from "../../../../environments/environment";
import {ChatRequest, ChatResponse} from "../../models/chat";

export interface MessageResponse {
  message: string
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(private http: HttpClient) {
  }

  chatBaseUrl = `${environment.baseUri}/chat/web`
  headers = new HttpHeaders().set('ngrok-skip-browser-warning','6024')

  getChatId(): Observable<ChatId> {
    return this.http.get<ChatId>(this.chatBaseUrl, {headers: this.headers})
  }

  sendMessage(request: ChatRequest): Observable<ChatResponse> {
    return this.http.post<any>(this.chatBaseUrl, request, {headers: this.headers})
  }
}
