import {Component} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';

@Component({
  selector: 'progress-bar',
  templateUrl: './progress-bar.component.html',
  styleUrls: ['./progress-bar.component.css']
})
export class ProgressBarComponent {
  constructor(private axaService: AxaServiceService) {}

  ngOnInit(): void {

  }
  getProgress(){
      
  }

}
