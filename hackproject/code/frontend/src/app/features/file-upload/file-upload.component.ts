import {Component} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {MatDialogRef} from "@angular/material/dialog";
import {FileUploadService} from "../../shared/services/file-upload/file-upload.service";
import {Document, FileUploadRequest} from "../../shared/models/file-upload";
import {SharedService} from "../../shared/services/shared/shared.service";
import {tap} from "rxjs";


@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent {
  selectedFile!: File;

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

  uploadFileForm: FormGroup = this.formBuilder.group({
    type: this.formBuilder.control('', Validators.required),
    doc_language: this.formBuilder.control('', Validators.required),
    native_language: this.formBuilder.control(this.sharedService.nativeLanguage, Validators.required)
  })

  categories: string [] = []
  languages: string[] = []

  cancel() {
    this.dialog.close()
  }

  uploadFile() {
    const chatId = this.sharedService.chatId
    if (!chatId) return
    const formData = new FormData();
    formData.append("type", this.uploadFileForm.value["type"]);
    formData.append("doc_language", this.uploadFileForm.value["doc_language"]);
    formData.append("native_language", this.uploadFileForm.value["native_language"]);
    formData.append("chat_id", chatId);
    formData.append('file', this.sharedService.file, this.sharedService.file.name);
    const request = formData
    console.log(request)
    this.sharedService.startNewChat()
    this.dialog.close()
    this.fileService.uploadDocument(request)
      .subscribe((res) => {
        this.sharedService.addFileUploadResponse(res)
      })
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

  onFileInputChange(event: any) {
    const files = event.target.files;
    if (files && files.length > 0) {
      this.selectedFile = files[0];
      this.sharedService.file = this.selectedFile;
    }
  }
}
