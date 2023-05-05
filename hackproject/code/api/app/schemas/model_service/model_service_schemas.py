from pydantic import BaseModel

class InsuranceDocumentResponse(BaseModel):
    summary: str
    included_in_cover: str
    excluded_from_cover: str
    emergency_information: str

class LandDocumentResponse(BaseModel):
    summary: str
    description: str
    terms_of_use: str
    warranties_and_guarantees: str

class ServiceContractDocumentResponse(BaseModel):
    summary: str
    payment_and_services: str
    obligations: str
    liability: str

class EmploymentContractDocumentResponse(BaseModel):
    summary: str
    start_date: str
    benefits_and_packages: str
    schedule: str
    response_deadline: str

class ConfidentialityAgreementDocumentResponse(BaseModel):
    summary: str
    confidential_info: str
    timeframe: str
    breach: str
    obligations: str
    steps_upon_violation: str

class SalesContractDocumentResponse(BaseModel):
    summary: str
    coverage: str
    payment_plan: str
    details_of_delivery: str

class IndependentContractorAgreementDocumentResponse(BaseModel):
    summary: str
    schedule: str
    payment_terms: str
    details_of_termination: str

class LoanAgreementDocumentResponse(BaseModel):
    summary: str
    loan_amount: str
    interest_rate: str
    timeframe: str
    method_of_repayment: str
    late_payment_info: str

class PartnershipAgreementDocumentResponse(BaseModel):
    summary: str
    responsibilities: str
    restrictions: str
    dispute_resolution: str

class PromptResponse(BaseModel):
    prompt: str
    response: str