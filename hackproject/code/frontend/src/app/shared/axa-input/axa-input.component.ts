import {Component} from '@angular/core';
import { ComputerAnswer } from '../models/chat';
import { AxaServiceService } from '../services/axa/axa-service.service';

@Component({
  selector: 'axa-input',
  templateUrl: './axa-input.component.html',
  styleUrls: ['./axa-input.component.css']
})
export class AXAInputComponent {
  currentQuestion:any
  questionPayload: ComputerAnswer = {  id: "string", value: "string", order: 0}

  constructor(private axaService:AxaServiceService) {
  }

  ngOnInit(): void {
    this.getCurrentQuestion()
  }

  sendResponse(){
    this.axaService.computeAnswer(this.questionPayload).subscribe(data => console.log(data))
    location.reload()
  }

  getCurrentQuestion(){
    this.axaService.getProductsQuestion().subscribe(
      data=>{this.currentQuestion=data;
      console.log(data)
    }
      )
  }
}
