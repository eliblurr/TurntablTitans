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
import {MatSelectModule} from "@angular/material/select";


@NgModule({
  declarations: [
    TopNavbarComponent,MainLayoutComponent, SidebarComponent

  ],
    imports: [
        CommonModule,
        SharedRoutingModule, NgSelectModule, FormsModule, ReactiveFormsModule, MatSidenavModule,
        MatListModule, MatExpansionModule, MatIconModule, MatButtonModule, MatTooltipModule, MatCheckboxModule,
        MatOptionModule, MatSelectModule
    ],
  exports:[MainLayoutComponent, NgSelectModule, FormsModule, ReactiveFormsModule]
})
export class SharedModule { }
