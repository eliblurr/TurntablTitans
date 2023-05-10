export interface Document {
  type: string
  doc_language: string
  file_path: string
  native_language: string
}

export interface FileUploadRequest {
  prompt: Document
  chat_id: string
}

export interface Language {
  languages: string[]
}

export interface FileTypes{
    doc_types: string[]
}

export interface FileResponse {
  title: string
  message: string
}
