import {Component} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';

@Component({
  selector: 'axa-input',
  templateUrl: './axa-input.component.html',
  styleUrls: ['./axa-input.component.css']
})
export class AXAInputComponent {
  currentQuestion:any
  event =  {
    "id": "string",
    "value": "string",
    "order": 0
  }

  constructor(private axaService:AxaServiceService) {
  }

  ngOnInit(): void {
    this.getCurrentQuestion()
  }

  sendResponse(){
    this.axaService.computeAnswer(this.event).subscribe(data => console.log(data))
  }

  getCurrentQuestion(){
    this.axaService.getProductsQuestion().subscribe(
      data=>{this.currentQuestion=data;
      console.log(data)
    }
      )
  }
}
