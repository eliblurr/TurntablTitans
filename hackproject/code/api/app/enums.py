from enum import Enum


class Document(Enum):
    INSURANCE = 'INSURANCE'
    LAND = 'LAND'
    SERVICE_CONTRACT = 'SERVICE_CONTRACT'
    EMPLOYMENT_CONTRACT = 'EMPLOYMENT_CONTRACT'
    CONFIDENTIALITY_AGREEMENT = 'CONFIDENTIALITY_AGREEMENT'
    SALES_CONTRACT = 'SALES_CONTRACT'
    INDEPENDENT_CONTRACTOR_AGREEMENT = 'INDEPENDENT_CONTRACTOR_AGREEMENT'
    LOAN_AGREEMENT = 'LOAN_AGREEMENT'
    PARTNERSHIP_AGREEMENT = 'PARTNERSHIP_AGREEMENT'

class Prompts(Enum):
    SUMMARY = "Can you give me a summary of the document using easy to understand words or non-legal terms"
    INSURANCE = {
        "included_in_cover" : "What is included in the cover?",
        "excluded_from_cover" : "What is excluded from the cover?",
        "emergency_information" :"Who should I contact in case of emergency?"
    }
    LAND = {
        "description" : "Describe the property briefly?",
        "terms_of_use" : "What are the terms of use?",
        "warranties_and_guarantees" : "What are the warranties and guarantees?"
    }
    SERVICE_CONTRACT = {
        "payment_and_services" : "How and what exactly is the vendor being paid for its services?",
        "obligations" : "What are my obligations?",
        "liability" : "How will be responsible for mistakes?"
    }
    EMPLOYMENT_CONTRACT = {
        "start_date" : "What is the start date?",
        "benefits_and_packages" : "What are the benefits and packages?",
        "schedule" : "Is there a defined schedule?",
        "response_deadline" :"Am I expected to give my answer before a certain date?"
    }
    CONFIDENTIALITY_AGREEMENT = {
        "confidential_info" : "What constitutes confidential information?",
        "timeframe" : "Within what timeframe does this agreement hold?",
        "breach" : "What constitutes a breach?",
        "obligations" : "What are my obligations?",
        "steps_upon_violation" : "What steps will be taken if I violate?"
    }
    SALES_CONTRACT = {
        "coverage" : "What are the goods and services covered?",
        "payment_plan" : "Is there a payment plan in place?",
        "details_of_delivery" : "What are the details of delivery?"
    }
    INDEPENDENT_CONTRACTOR_AGREEMENT = {
        "schedule" : "Will I be required to work a set schedule?",
        "payment_terms" : "What are the payment terms?",
        "details_of_termination" : "What is the minimum notice which will be provided in case of an,"
                                                     "early contract termination?"
    }
    LOAN_AGREEMENT = {
        "loan_amount" : "What is the loan amount?",
        "interest_rate" : "What is the interest rate?",
        "timeframe" : "What is the timeframe of the agreement?",
        "method_of_repayment" : "What is the method of repayment?",
        "late_payment_info" :"What happens in case there are late or missed payments?"
    }
    PARTNERSHIP_AGREEMENT = {
        "responsibilities" : "What are the responsibilities of the partners?",
        "restrictions" : "What are the restriction on partners",
        "dispute_resolution" : "What will disputes be resolved"
    }

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v