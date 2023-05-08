import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedRoutingModule } from './shared-routing.module';
import { TopNavbarComponent } from './top-navbar/top-navbar.component';
import {MainLayoutComponent} from "./main-layout/main-layout.component";
import { NgSelectModule } from '@ng-select/ng-select';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { SidebarComponent } from './sidebar/sidebar.component';
import {MatSidenavModule} from "@angular/material/sidenav";
import {MatListModule} from "@angular/material/list";
import {MatExpansionModule} from "@angular/material/expansion";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {MatTooltipModule} from "@angular/material/tooltip";
import {MatCheckboxModule} from "@angular/material/checkbox";
import { MatOptionModule } from '@angular/material/core';
import {RecorderComponent} from './recorder/recorder.component'
import { AccordionComponent } from './accordion/accordion.component';
import { ProgressBarComponent } from './progress-bar/progress-bar.component';
import { ComputeAnswerComponent } from './compute-answer/compute-answer.component';
import { QuestionsComponent } from './questions/questions.component';
import { AXADocsComponent } from './axa-docs/axa-docs.component';
import { AXAInputComponent } from './axa-input/axa-input.component';

@NgModule({
  declarations: [
    TopNavbarComponent,MainLayoutComponent, SidebarComponent, RecorderComponent, AccordionComponent, ProgressBarComponent,
    ComputeAnswerComponent, QuestionsComponent, AXADocsComponent, AXAInputComponent
  ],
    imports: [
        CommonModule,
        SharedRoutingModule, NgSelectModule, FormsModule, ReactiveFormsModule, MatSidenavModule, 
        MatListModule, MatExpansionModule, MatIconModule, MatButtonModule, MatTooltipModule, MatCheckboxModule,
        MatOptionModule
    ],
  exports:[MainLayoutComponent, NgSelectModule, FormsModule, ReactiveFormsModule]
})
export class SharedModule { }
