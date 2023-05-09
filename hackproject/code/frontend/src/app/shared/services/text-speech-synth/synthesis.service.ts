import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import { catchError, retry } from 'rxjs/operators';
import {TTS} from "../../models/synth";
import {environment} from "../../../../environments/environment";
// import {ChatRequest, ChatResponse} from "../../models/chat";

export interface MessageResponse {
  message: string
}

@Injectable({
  providedIn: 'root'
})
export class SynthesisService {

  constructor(private http: HttpClient) {
  }

  BaseUrl = `${environment.baseUri}`
  headers = new HttpHeaders().set('ngrok-skip-browser-warning','6024')

  fetch_audio(payload:TTS, message_id:string): Observable<any> {
    return this.http.post<any>(`${this.BaseUrl}/tts/${message_id}`, payload, {headers: this.headers, responseType:'blob' as 'json'})
  }

  // fetch_text(text:string, message_id:string): Observable<any> {
  //   return this.http.post<any>(`${this.BaseUrl}/tts/${message_id}`, {headers: this.headers})
  // }

//   getChatId(): Observable<ChatId> {
//     return this.http.get<ChatId>(this.chatBaseUrl, {headers: this.headers})
//   }

//   sendMessage(request: ChatRequest): Observable<ChatResponse> {
//     return this.http.post<any>(this.chatBaseUrl, request, {headers: this.headers})
//   }
}
