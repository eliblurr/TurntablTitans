import { Component } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {MatDialogRef} from "@angular/material/dialog";
import {FileUploadService} from "../../shared/services/file-upload/file-upload.service";
import {File, FileUploadRequest} from "../../shared/models/file-upload";


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
    type: this.formBuilder.control('', Validators.required),
    doc_language: this.formBuilder.control('', Validators.required),
    file_path: this.formBuilder.control('', Validators.required),
    native_language: this.formBuilder.control('English', Validators.required)
  })

  categories: string [] = []

  languages: string[] = []

  cancel() {
    this.dialog.close()
  }

  uploadFile() {
    const chatId = localStorage.getItem('chat_id')
    if(!chatId) return
    const request: FileUploadRequest = {prompt: this.uploadFileForm.value, chat_id:chatId}
    this.fileService.uploadDocument(request)

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
