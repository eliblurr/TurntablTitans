import {Component, Input} from '@angular/core';
import {FileResponse} from "../models/file-upload";

@Component({
  selector: 'accordion',
  templateUrl: './accordion.component.html',
  styleUrls: ['./accordion.component.css']
})
export class AccordionComponent {
  @Input() fileResponse!: FileResponse

  constructor(
  ) {
  }

  ngOnInit(): void {
  }

}
