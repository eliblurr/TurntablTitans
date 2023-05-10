import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ComputerAnswer } from '../../models/chat';

@Injectable({
  providedIn: 'root'
})
export class AxaServiceService {

  constructor(private http: HttpClient) { }
  productID:any = localStorage.getItem("currentProducyID")
  questionID:any = localStorage.getItem("currentQuestionID")
  axaProductsURL = `${environment.baseUri}/axa/products`
  axaQuestionsURL = `${environment.baseUri}/axa/`+this.productID+`/questions`
  axaQuestionInputURL = `${environment.baseUri}/axa/`+this.productID+`/questions/`+this.questionID
  axaComputeURL = `${environment.baseUri}/axa/`+this.productID+`/compute`


  headers = new HttpHeaders().set('ngrok-skip-browser-warning','6024')

  getProgress(): Observable<any> {
    return this.http.get<any>(this.axaQuestionsURL, {headers: this.headers})
  }

  getQuestions(): Observable<any> {
    return this.http.get<any>(this.axaQuestionsURL, {headers: this.headers})
  }
  getProducts(): Observable<any> {
    return this.http.get<any>(this.axaProductsURL, {headers: this.headers})
  }
  getProductsQuestion(): Observable<any> {
    return this.http.get<any>(this.axaQuestionInputURL, {headers: this.headers})
  }

  getQuestionById(id: string): Observable<any> {
    return this.http.get<any>(this.axaQuestionsURL+`/${id}`, {headers: this.headers})
  }

  computeAnswer(request: ComputerAnswer[]): Observable<any> {
    return this.http.post<any>(this.axaComputeURL, request, {headers: this.headers})
  }
}
