export interface File{
  type: string
  doc_language: string
  file_path: string
  native_language: string
}

export interface FileUploadRequest {
  prompt: File
  chat_id: string
}

export interface Language{
  languages:string[]
}

export interface FileTypes{
    doc_types: string[]
}

export interface InsuranceDocumentResponse{
  summary: string
  included_in_cover: string
  excluded_from_cover: string
  emergency_information: string
}

export interface LandDocumentResponse{
  summary: string
  description: string
  terms_of_use: string
  warranties_and_guarantees: string
}

export interface ServiceContractDocumentResponse{
  summary: string
  payment_and_services: string
  obligations: string
  liability: string
}

export interface EmploymentContractDocumentResponse{
  summary: string
  start_date: string
  benefits_and_packages: string
  schedule: string
  response_deadline: string
}

export interface ConfidentialityAgreementDocumentResponse{
  summary: string
  confidential_info: string
  timeframe: string
  breach: string
  obligations: string
  steps_upon_violation: string
}

export interface SalesContractDocumentResponse{
  summary: string
  coverage: string
  payment_plan: string
  details_of_delivery: string
}

export interface IndependentContractorAgreementResponse {
  summary: string
  schedule: string
  payment_terms: string
  details_of_termination: string
}

export interface LoanAgreementDocumentResponse{
  summary: string
  loan_amount: string
  interest_rate: string
  timeframe: string
  method_of_repayment: string
  late_payment_info: string
}

export interface PartnershipAgreementDocumentResponse{
  summary: string
  responsibilities: string
  restrictions: string
  dispute_resolution: string
}
