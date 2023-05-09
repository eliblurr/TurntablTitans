import {Component} from '@angular/core';
import { SidebarService } from '../services/sidebar/sidebar.service';

@Component({
  selector: 'axa-docs',
  templateUrl: './axa-docs.component.html',
  styleUrls: ['./axa-docs.component.css']
})
export class AXADocsComponent {
  constructor(public sidebarService: SidebarService){
  }

  ngOnInit(): void {
  }

}
