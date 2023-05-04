import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

export interface MessageResponse{
  message: string
}
@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(private http: HttpClient) { }

  // sendMessage(message: string):Observable<MessageResponse>{
  //   return this.http.post<MessageResponse>('http://localhost:5050/api/v1/message', {message})
  // }

  sendMessage(message: string):Observable<MessageResponse>{
    const response = {message: "Turntabl Titans to the rescue"}
    return new Observable(observer => {
      setTimeout(() => {
        observer.next(response);
        observer.complete();
      }, 200);
    });
  }
}
