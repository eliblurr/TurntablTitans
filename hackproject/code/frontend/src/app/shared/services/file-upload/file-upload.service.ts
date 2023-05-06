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
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {

  constructor(
    private http: HttpClient
  ) {
  }

  fileBaseUrl = "http://127.0.0.1:8000/api/v1/chat/web"
  languageBaseUrl = "http://127.0.0.1:8000/api/v1/languages"
  fileTypeBaseUrl = "http://127.0.0.1:8000/api/v1/documents"

  getFileTypes() {
    return this.http.get<FileTypes>(this.fileTypeBaseUrl)
  }

  getLanguages(): Observable<Language> {
    return this.http.get<Language>(this.languageBaseUrl)
  }

  uploadDocument(request: FileUploadRequest): Observable<any> {
    return this.http.post<any>(this.fileBaseUrl, request)
  }
  
  uploadInsuranceDocument(request: FileUploadRequest): Observable<InsuranceDocumentResponse> {
    return this.http.post<InsuranceDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadLandDocument(request: FileUploadRequest): Observable<LandDocumentResponse> {
    return this.http.post<LandDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadServiceContract(request: FileUploadRequest): Observable<ServiceContractDocumentResponse> {
    return this.http.post<ServiceContractDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadEmploymentContract(request: FileUploadRequest): Observable<EmploymentContractDocumentResponse> {
    return this.http.post<EmploymentContractDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadConfidentialityAgreementDocument(request: FileUploadRequest): Observable<ConfidentialityAgreementDocumentResponse> {
    return this.http.post<ConfidentialityAgreementDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadSalesContractDocument(request: FileUploadRequest): Observable<SalesContractDocumentResponse> {
    return this.http.post<SalesContractDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadIndependentContractorAgreementDocument(request: FileUploadRequest): Observable<IndependentContractorAgreementResponse> {
    return this.http.post<IndependentContractorAgreementResponse>(this.fileBaseUrl, request)
  }

  uploadLoanAgreementDocumentResponse(request: FileUploadRequest): Observable<LoanAgreementDocumentResponse> {
    return this.http.post<LoanAgreementDocumentResponse>(this.fileBaseUrl, request)
  }

  uploadPartnershipAgreementDocument(request: FileUploadRequest): Observable<PartnershipAgreementDocumentResponse> {
    return this.http.post<PartnershipAgreementDocumentResponse>(this.fileBaseUrl, request)
  }

}
