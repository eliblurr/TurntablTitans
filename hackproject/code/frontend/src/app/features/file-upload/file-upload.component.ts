import { Component } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {MatDialogRef} from "@angular/material/dialog";
import {FileUploadService} from "../../shared/services/file-upload/file-upload.service";

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent {
  constructor(
    private formBuilder: FormBuilder,
    private fileService: FileUploadService,
    private dialog: MatDialogRef<FileUploadComponent>,

  ) {
  }

  ngOnInit(): void {
    this.getFileTypes()
    this.getLanguages()
  }

  uploadFileForm: FormGroup = this.formBuilder.group({
    file: this.formBuilder.control('', Validators.required),
    category: this.formBuilder.control(null, Validators.required),
    language: this.formBuilder.control('', Validators.required)
  })
  categories: string [] = [
    
  ]

  languages: string[] = [
    
  ]

  cancel() {
    this.dialog.close()
  }

  uploadFile() {
  console.log(this.uploadFileForm.value)
  }

  getFileTypes(){
    this.fileService.getFileTypes().subscribe(
      (res) => this.categories = res.doc_types
    )
  }

  getLanguages(){
    this.fileService.getLanguages().subscribe(
      (res) => this.languages = res.languages
    )
  }
}
