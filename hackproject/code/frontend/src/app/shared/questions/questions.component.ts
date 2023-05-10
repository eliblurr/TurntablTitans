import {Component} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';

@Component({
  selector: 'questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css']
})
export class QuestionsComponent {
  question:any
  constructor(private axaService:AxaServiceService) {}

  ngOnInit(): void {
    this.getAXAQuestions();
  }

  getAXAQuestions(){
    this.axaService.getQuestions().subscribe(data =>
      {this.question=data});}
      
  parseQuestionID(id:any){
    localStorage.setItem("currentQuestionID",id)
    location.reload()
  }
}
