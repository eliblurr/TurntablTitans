import {Component, Input, Output, EventEmitter, OnChanges, SimpleChanges} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';
import { ActivatedRoute } from '@angular/router';
import { SharedService } from '../services/shared/shared.service';


@Component({
  selector: 'questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css']
})
export class QuestionsComponent implements OnChanges {
  @Input() questions!:any 
  @Input() currentQuestion!:any 
  @Output() idEmitter = new EventEmitter<any>();    

  constructor(private route: ActivatedRoute, public sharedService: SharedService){}

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges) {
    this.questions = changes["questions"].currentValue; 
    this.scrollToElement(this.questions['id'])
  }

  passQuestionID(id:any){
    this.idEmitter.emit(id);  
  }

  scrollToElement(id:string) {
  console.log(`scrolling to ${id}`);
  let el = document.getElementById(id);
  if (el !=null){
    el.scrollIntoView()
  }
  // el.scrollIntoView();
}

  textToSpeech(text:string){
    this.sharedService.textToSpeech(text, "en")
  }


}
