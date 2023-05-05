import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { DragDropModule } from '@angular/cdk/drag-drop';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MatIconModule } from '@angular/material/icon';
import { HttpClientModule } from '@angular/common/http';
import {FileUploadComponent} from "./features/file-upload/file-upload.component";
import {MatDialog, MatDialogModule} from "@angular/material/dialog";
import {MatButtonModule} from "@angular/material/button";
import {ReactiveFormsModule} from "@angular/forms";
import {MatSelectModule} from "@angular/material/select";


@NgModule({
  declarations: [
    AppComponent,
    FileUploadComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    DragDropModule,
    MatIconModule,
    HttpClientModule,
    MatDialogModule,
    MatButtonModule,
    MatSelectModule,
    ReactiveFormsModule,
    NoopAnimationsModule
  ],
  providers: [],
  entryComponents:[FileUploadComponent],
  bootstrap: [AppComponent]
})
export class AppModule { }
