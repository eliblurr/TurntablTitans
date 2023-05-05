import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FeaturesRoutingModule } from './features-routing.module';
import { FileUploadComponent } from './file-upload/file-upload.component';
import {MatDialogModule} from "@angular/material/dialog";
import {ReactiveFormsModule} from "@angular/forms";
import {MatSelectModule} from "@angular/material/select";


@NgModule({
  declarations: [
    FileUploadComponent
  ],
  imports: [
    CommonModule,
    FeaturesRoutingModule,
    MatDialogModule,
    ReactiveFormsModule,
    MatSelectModule
  ]
})
export class FeaturesModule { }
