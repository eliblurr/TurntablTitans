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