import { Component } from '@angular/core';
import { SidebarService } from '../services/sidebar/sidebar.service';
import { AxaServiceService } from '../services/axa/axa-service.service';
import { ComputerAnswer } from '../models/chat' 

@Component({
  selector: 'app-axa-layout',
  templateUrl: './axa-layout.component.html',
  styleUrls: ['./axa-layout.component.css']
})
export class AxaLayoutComponent {
  opens = this.sideBarService.collapseSideBar
  questions:any =[]
  answers: Array<ComputerAnswer> = []
  coverage:any = []
  progress: any = null
  currentQuestionId: any = null

  constructor(
    public sideBarService:SidebarService,
    private axaService:AxaServiceService
  ) { }

  ngOnInit(): void {
    this.getAXAQuestions();
  }

  getAXAQuestions(){
    this.axaService.getQuestions().subscribe(data =>{
      this.questions=data;  
      if (data.length > 0){
        this.setStartQuestion(data[0]['id'])
      }
    });
  }

  setStartQuestion(id:string){this.currentQuestionId = id}

  getQuestionIdFromChild($event: string){
    this.currentQuestionId = $event
  }

  getAnswerFromChild($event: any){
    const obj: ComputerAnswer = {"id":$event['id'], "value":$event['answer'], "order":this.answers.length+1}
    console.log($event)
    this.answers.push(obj)
    this.axaService.computeAnswer(this.answers).subscribe(
      data=>{
        console.log(data)
        this.progress = data['progress']
        this.answers=data['states']
        this.coverage = data['coverage']
        console.log( data['next_question'])
        this.currentQuestionId=data['next_question']!=null? data['next_question']['id']: null
      }
    )
  }

}
