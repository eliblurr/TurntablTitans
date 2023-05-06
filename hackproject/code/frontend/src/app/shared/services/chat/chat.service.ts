import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Chat} from "../../models/chat";

export interface MessageResponse {
  message: string
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(private http: HttpClient) {
  }

  chatBaseUrl = "http://127.0.0.1:8000/api/v1/chat/web"

  getChatId(): Observable<Chat> {
    return this.http.get<Chat>(this.chatBaseUrl)
  }

  // sendMessage(message: string):Observable<MessageResponse>{
  //   return this.http.post<MessageResponse>('http://localhost:5050/api/v1/message', {message})
  // }

  sendMessage(message: string): Observable<MessageResponse> {
    const response = {message: "Turntabl Titans to the rescue"}
    return new Observable(observer => {
      setTimeout(() => {
        observer.next(response);
        observer.complete();
      }, 200);
    });
  }
}
