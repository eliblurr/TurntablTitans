from pydantic import BaseModel

class InsuranceDocumentResponse(BaseModel):
    Summary: str
    What_is_included_in_cover: str
    What_is_excluded_from_cover: str
    Who_to_contact_in_case_of_emergency: str

class LandDocumentResponse(BaseModel):
    Summary: str
    Description_of_property: str
    Terms_of_use: str
    Warranties_and_guarantees: str

class ServiceContractDocumentResponse(BaseModel):
    Summary: str
    Terms_of_payment_and_services: str
    Obligations: str
    Liabilities: str

class EmploymentContractDocumentResponse(BaseModel):
    Summary: str
    Start_date: str
    Benefits_and_packages: str
    Schedule: str
    Response_deadline: str

class ConfidentialityAgreementDocumentResponse(BaseModel):
    Summary: str
    What_constitutes_confidential_information: str
    Timeframe_within_which_the_agreement_holds: str
    What_constitutes_a_breach: str
    Obligations: str
    What_steps_will_be_taken_if_I_violate: str

class SalesContractDocumentResponse(BaseModel):
    Summary: str
    What_goods_and_services_are_covered: str
    Is_there_a_payment_plan: str
    Details_of_delivery: str

class IndependentContractorAgreementDocumentResponse(BaseModel):
    Summary: str
    Will_I_be_required_to_work_a_set_schedule: str
    Payment_terms: str
    Details_of_termination: str

class LoanAgreementDocumentResponse(BaseModel):
    Summary: str
    Loan_amount: str
    Interest_rate: str
    Repayment_timeframe: str
    Mode_of_repayment: str
    What_happens_in_case_of_late_or_missed_payments: str

class PartnershipAgreementDocumentResponse(BaseModel):
    Summary: str
    Responsibilities_of_parties: str
    Restrictions_on_partners: str
    How_disputes_will_be_resolved: str

class PromptResponse(BaseModel):
    prompt: str
    response: str