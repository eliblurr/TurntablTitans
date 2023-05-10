import {Component, Input} from '@angular/core';
import {FileResponse} from "../models/file-upload";
import {SharedService} from "../services/shared/shared.service";

@Component({
  selector: 'accordion',
  templateUrl: './accordion.component.html',
  styleUrls: ['./accordion.component.css']
})
export class AccordionComponent {
  @Input() fileResponse!: FileResponse
  @Input() title!: string

  constructor(
    private sharedService: SharedService,
  ) {}

  ngOnInit(): void {
  }

  textToSpeech(text: string) {
    this.sharedService.textToSpeech(text, "en")
  }

}
