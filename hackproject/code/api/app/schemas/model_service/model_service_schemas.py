from pydantic import BaseModel

class InsuranceDocumentResponseSchema(BaseModel):
    summary: str
    included_in_cover: str
    excluded_from_cover: str
    emergency_information: str

class LandDocumentResponseSchema(BaseModel):
    summary: str
    description: str
    terms_of_use: str
    warranties_and_guarantees: str

class ServiceContractDocumentResponseSchema(BaseModel):
    summary: str
    payment_and_services: str
    obligations: str
    liability: str

class EmploymentContractDocumentResponseSchema(BaseModel):
    summary: str
    start_date: str
    benefits_and_packages: str
    schedule: str
    response_deadline: str

class ConfidentialityAgreementDocumentResponseSchema(BaseModel):
    summary: str
    confidential_info: str
    timeframe: str
    breach: str
    obligations: str
    steps_upon_violation: str

class SalesContractDocumentResponseSchema(BaseModel):
    summary: str
    coverage: str
    payment_plan: str
    details_of_delivery: str

class IndependentContractorAgreementDocumentResponseSchema(BaseModel):
    summary: str
    schedule: str
    payment_terms: str
    details_of_termination: str

class LoanAgreementDocumentResponseSchema(BaseModel):
    summary: str
    loan_amount: str
    interest_rate: str
    timeframe: str
    method_of_repayment: str
    late_payment_info: str

class PartnershipAgreementDocumentResponseSchema(BaseModel):
    summary: str
    responsibilities: str
    restrictions: str
    dispute_resolution: str