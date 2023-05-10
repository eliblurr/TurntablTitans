import {Component, Input, OnChanges, SimpleChanges} from '@angular/core';

@Component({
  selector: 'compute-answer',
  templateUrl: './compute-answer.component.html',
  styleUrls: ['./compute-answer.component.css']
})
export class ComputeAnswerComponent implements OnChanges {
  @Input() coverage: any = []
  constructor() {}
  ngOnChanges(changes: SimpleChanges): void {
    this.coverage = changes["coverage"].currentValue; 
  }
  ngOnInit(): void {}
}
