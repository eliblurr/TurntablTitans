import {Injectable} from '@angular/core';
import {
  ConfidentialityAgreementDocumentResponse,
  EmploymentContractDocumentResponse, FileTypes,
  FileUploadRequest,
  IndependentContractorAgreementResponse,
  InsuranceDocumentResponse,
  LandDocumentResponse, Language,
  LoanAgreementDocumentResponse,
  PartnershipAgreementDocumentResponse,
  SalesContractDocumentResponse,
  ServiceContractDocumentResponse
} from "../../models/file-upload";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {environment} from "../../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {

  constructor(
    private http: HttpClient
  ) {
  }

  fileBaseUrl = `${environment.baseUri}/file/web`
  languageBaseUrl = `${environment.baseUri}/languages`
  fileTypeBaseUrl = `${environment.baseUri}/documents`
  headers = new HttpHeaders().set('ngrok-skip-browser-warning','6024')

  getFileTypes() {
    return this.http.get<FileTypes>(this.fileTypeBaseUrl, {headers: this.headers})
  }

  getLanguages(): Observable<Language> {

    return this.http.get<Language>(this.languageBaseUrl, {headers: this.headers})
  }

  uploadDocument(request: FormData): Observable<any> {
    return this.http.post<any>(this.fileBaseUrl, request, {headers: this.headers})
  }
}
