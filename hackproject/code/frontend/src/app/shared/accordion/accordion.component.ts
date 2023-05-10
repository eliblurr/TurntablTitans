import {Component, Input} from '@angular/core';
import {FileResponse} from "../models/file-upload";
import { SharedService } from '../services/shared/shared.service';

@Component({
  selector: 'accordion',
  templateUrl: './accordion.component.html',
  styleUrls: ['./accordion.component.css']
})
export class AccordionComponent {
  @Input() fileResponse!: FileResponse
  @Input() index!: any

  constructor(
    private sharedService:SharedService
  ) {
  }

  textToSpeech(text: string) {
    this.sharedService.textToSpeech(text, "en")
  }

  ngOnInit(): void {
  }

}
