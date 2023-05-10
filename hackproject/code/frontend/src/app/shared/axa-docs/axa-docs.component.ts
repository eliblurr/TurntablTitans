import {Component} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';
import { SidebarService } from '../services/sidebar/sidebar.service';

@Component({
  selector: 'axa-docs',
  templateUrl: './axa-docs.component.html',
  styleUrls: ['./axa-docs.component.css']
})
export class AXADocsComponent {
  product:any
  constructor(public sidebarService: SidebarService, private axaService:AxaServiceService){
  }

  getAvailableProducts(){
    this.axaService.getProducts().subscribe(data =>
      {
      console.log(data)
      this.product=data});
  
  }
  getQuestions(id:any){
    console.log(id)
    localStorage.setItem('currentProducyID', id)
    location.reload()
  }

  ngOnInit(): void {
    this.getAvailableProducts();
  }

}
