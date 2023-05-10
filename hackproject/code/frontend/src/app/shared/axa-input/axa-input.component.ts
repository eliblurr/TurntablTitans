import {Component, Input, Output, OnChanges, SimpleChanges, EventEmitter} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';
import { SharedService } from '../services/shared/shared.service';

@Component({
  selector: 'axa-input',
  templateUrl: './axa-input.component.html',
  styleUrls: ['./axa-input.component.css']
})
export class AXAInputComponent implements OnChanges {
  @Input() currentQuestionId:any
  @Output() answerEmitter = new EventEmitter<any>(); 
  currentQuestion: any
  inputAreaValue: any

  constructor(private axaService:AxaServiceService, 
   public sharedService: SharedService,) {
  }

  ngOnChanges(changes: SimpleChanges): void {
    this.currentQuestion=null
    this.getQuestionById(changes['currentQuestionId'].currentValue);
  }

  submit(){    
    this.answerEmitter.emit({"answer":this.inputAreaValue, "id":this.currentQuestion['id']})
    this.inputAreaValue = null
    this.currentQuestion = null
  }

  updateInput(answer:string){
    this.inputAreaValue = null
    this.inputAreaValue = answer
  }

  getQuestionById(id:string){
    this.axaService.getQuestionById(id).subscribe(
      data=>{
        this.currentQuestion=data;
        console.log(data)
      }
    )
  }

  textToSpeech(text:string){
    this.sharedService.textToSpeech(text, "en")
  }

}
