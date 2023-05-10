import {Component, Input, OnChanges, SimpleChanges} from '@angular/core';
import { AxaServiceService } from '../services/axa/axa-service.service';

@Component({
  selector: 'progress-bar',
  templateUrl: './progress-bar.component.html',
  styleUrls: ['./progress-bar.component.css']
})
export class ProgressBarComponent implements OnChanges  {
  @Input() progress: any = 0;
  constructor(private axaService: AxaServiceService) {}
  
  ngOnChanges(changes: SimpleChanges): void {
    console.log(changes)
  }

  ngOnInit(): void {

  }
  getProgress(){
      
  }

}
