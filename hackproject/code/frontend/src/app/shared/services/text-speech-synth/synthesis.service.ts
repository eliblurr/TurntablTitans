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
  // headers = new HttpHeaders().set('ngrok-skip-browser-warning','6024')
  

  fetch_audio(payload:TTS, message_id:string): Observable<any> {
    return this.http.post<any>(`${this.BaseUrl}/tts/${message_id}`, payload, {headers: new HttpHeaders().set('ngrok-skip-browser-warning','6024'), responseType:'blob' as 'json'})
  }

  fetch_text(blob:Blob, fileName:string, chatId:string):Observable<string>{
    const formData = new FormData();
    const headers = new HttpHeaders();
    const file = new File([blob], fileName, {type:'audio/wav'});

    // headers
    headers.set('ngrok-skip-browser-warning','6024')
    headers.set('Content-Type', "multipart/form-data")
   
    // form
    formData.append("chat_id", chatId);
    formData.append("native_language", "ENGLISH");
    formData.append("audio", file, fileName)

    return this.http.post<any>(
      `${this.BaseUrl}/stt`, 
      formData, 
      { headers: headers}
    )
  }

}
