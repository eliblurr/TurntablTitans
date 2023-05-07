import {Component} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {MatDialogRef} from "@angular/material/dialog";
import {FileUploadService} from "../../shared/services/file-upload/file-upload.service";
import {File, FileUploadRequest} from "../../shared/models/file-upload";
import {SharedService} from "../../shared/services/shared/shared.service";
import {tap} from "rxjs";


@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent {
  constructor(
    private formBuilder: FormBuilder,
    public sharedService: SharedService,
    private fileService: FileUploadService,
    private dialog: MatDialogRef<FileUploadComponent>,
  ) {
  }

  ngOnInit(): void {
    this.getFileTypes()
    this.getLanguages()
  }
  filepath = 'C:\\Users\\kwame.sarfo\\PycharmProjects\\finos-hackathon\\TurntablTitans\\hackproject\\code\\api\\app\\services\\model_service\\data\\motor.pdf';
  uploadFileForm: FormGroup = this.formBuilder.group({
    type: this.formBuilder.control('', Validators.required),
    doc_language: this.formBuilder.control('', Validators.required),
    file_path: this.formBuilder.control(this.filepath, Validators.required),
    native_language: this.formBuilder.control('ENGLISH', Validators.required)
  })

  categories: string [] = []
  languages: string[] = []

  cancel() {
    this.dialog.close()
  }

  uploadFile() {
    const chatId = this.sharedService.chatId
    console.log(chatId)
    if (!chatId) return
    const request: FileUploadRequest = {prompt: this.uploadFileForm.value, chat_id: chatId}
    this.sharedService.newFileName = 'Motor.pdf'
    this.sharedService.startNewChat()
    this.dialog.close()
    this.fileService.uploadDocument(request)
      .subscribe((res) => {
        this.sharedService.addFileUploadResponse(res)
        console.log(res)})
    console.log(this.uploadFileForm.value)
  }

  getFileTypes() {
    this.fileService.getFileTypes().subscribe(
      (res) => this.categories = res.doc_types
    )
  }

  getLanguages() {
    this.fileService.getLanguages().subscribe(
      (res) => this.languages = res.languages
    )
  }
}
