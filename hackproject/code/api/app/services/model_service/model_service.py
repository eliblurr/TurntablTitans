import os
from abc import abstractmethod
from llama_index import GPTSimpleVectorIndex
from hackproject.code.api.app.enums import Document
from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponseSchema, \
    LandDocumentResponseSchema, ServiceContractDocumentResponseSchema, EmploymentContractDocumentResponseSchema, \
    ConfidentialityAgreementDocumentResponseSchema, SalesContractDocumentResponseSchema, \
    IndependentContractorAgreementDocumentResponseSchema, LoanAgreementDocumentResponseSchema, \
    PartnershipAgreementDocumentResponseSchema
from dotenv import dotenv_values

class ModelService:
    @abstractmethod
    def process_prompt(self, prompt: str):
        pass

class ModelServiceImpl(ModelService):
    def __init__(self, document: str, type: Document, openai_api_key=None):
        if not openai_api_key:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            env_path = os.path.join(dir_path, '..', '..', '.env')
            config = dotenv_values(env_path)
            openai_api_key = config['OPENAI_API_KEY']
        os.environ['OPENAI_API_KEY'] = openai_api_key
        self.__index = GPTSimpleVectorIndex.from_documents(document)
        self.__document = type

    def process_document(self):
        match self.__document:
            case Document.INSURANCE:
                return self.__process_insurance_document()
            case Document.LAND:
                return self.__process_land_document()
            case Document.SERVICE_CONTRACT:
                return self.__process_service_contract_document()
            case Document.EMPLOYMENT_CONTRACT:
                return self.__process_employment_contract_document()
            case Document.CONFIDENTIALITY_AGREEMENT:
                return self.__process_confidentiality_agreement_document()
            case Document.SALES_CONTRACT:
                return self.__process_sales_contract_document()
            case Document.INDEPENDENT_CONTRACTOR_AGREEMENT:
                return self.__process_independent_contractor_agreement_document()
            case Document.LOAN_AGREEMENT:
                return self.__process_loan_agreement_document()
            case Document.PARTNERSHIP_AGREEMENT:
                return self.__process_partnership_agreement_document()


    def __generate_summary(self):
        return self.process_prompt("Can you give me a summary of the document using easy to understand words or"
                                   " non-legal terms")

    def process_prompt(self, prompt: str):
        return self.__index.query(prompt).response

    def __process_insurance_document(self):
        summary = self.__generate_summary()
        included_in_cover = self.process_prompt("What is included in the cover?")
        excluded_from_cover = self.process_prompt("What is excluded from the cover?")
        emergency_information = self.process_prompt("Who should I contact in case of emergency?")
        return InsuranceDocumentResponseSchema(summary=summary,
                                               included_in_cover=included_in_cover,
                                               excluded_from_cover=excluded_from_cover,
                                               emergency_information=emergency_information)

    def __process_land_document(self):
        summary = self.__generate_summary()
        description = self.process_prompt("Describe the property briefly")
        terms_of_use = self.process_prompt("What are the terms of use?")
        warranties_and_guarantees = self.process_prompt("What are the warranties and guarantees")
        return LandDocumentResponseSchema(summary=summary,
                                          description=description,
                                          terms_of_use=terms_of_use,
                                          warranties_and_guarantees=warranties_and_guarantees)

    def __process_service_contract_document(self):
        summary = self.__generate_summary()
        payment_and_services = self.process_prompt("How and what exactly is the vendor being paid for its services?")
        obligations = self.process_prompt("What are my obligations?")
        liability = self.process_prompt("How will be responsible for mistakes?")
        return ServiceContractDocumentResponseSchema(summary=summary,
                                                     payment_and_services=payment_and_services,
                                                     obligations=obligations,
                                                     liability=liability)

    def __process_employment_contract_document(self):
        summary = self.__generate_summary()
        start_date = self.process_prompt("What is the start date?")
        benefits_and_packages = self.process_prompt("What are the benefits and packages")
        schedule = self.process_prompt("Is there a defined schedule?")
        response_deadline = self.process_prompt("Am I expected to give my answer before a certain date?")
        return EmploymentContractDocumentResponseSchema(summary=summary,
                                                        start_date=start_date,
                                                        benefits_and_packages=benefits_and_packages,
                                                        schedule=schedule,
                                                        response_deadline=response_deadline)

    def __process_confidentiality_agreement_document(self):
        summary = self.__generate_summary()
        confidential_info = self.process_prompt("What constitutes confidential information?")
        timeframe = self.process_prompt("Within what timeframe does this agreement hold?")
        breach = self.process_prompt("What constitutes a breach?")
        obligations = self.process_prompt("What are my obligations?")
        steps_upon_violation = self.process_prompt("What steps will be taken if I violate")
        return ConfidentialityAgreementDocumentResponseSchema(summary=summary,
                                                              confidential_info=confidential_info,
                                                              timeframe=timeframe,
                                                              breach=breach,
                                                              obligations=obligations,
                                                              steps_upon_violation=steps_upon_violation)

    def __process_sales_contract_document(self):
        summary = self.__generate_summary()
        coverage = self.process_prompt("What are the goods and services covered?")
        payment_plan = self.process_prompt("Is there a payment plan in place?")
        details_of_delivery = self.process_prompt("What are the details of delivery?")
        return SalesContractDocumentResponseSchema(summary=summary,
                                                   coverage=coverage,
                                                   payment_plan=payment_plan,
                                                   details_of_delivery=details_of_delivery)

    def __process_independent_contractor_agreement_document(self):
        summary = self.__generate_summary()
        schedule = self.process_prompt("Will I be required to work a set schedule?")
        payment_terms = self.process_prompt("What are the payment terms?")
        details_of_termination = self.process_prompt("What is the minimum notice which will be provided in case of an,"
                                                  "early contract termination?")
        return IndependentContractorAgreementDocumentResponseSchema(summary=summary,
                                                                    schedule=schedule,
                                                                    payment_terms=payment_terms,
                                                                    details_of_termination=details_of_termination)

    def __process_loan_agreement_document(self):
        summary = self.__generate_summary()
        loan_amount = self.process_prompt("What is the loan amount?")
        interest_rate = self.process_prompt("What is the interest rate?")
        timeframe = self.process_prompt("What is the timeframe of the agreement?")
        method_of_repayment = self.process_prompt("What is the method of repayment?")
        late_payment_info = self.process_prompt("What happens in case there are late or missed payments?")
        return LoanAgreementDocumentResponseSchema(summary=summary,
                                                   loan_amount=loan_amount,
                                                   interest_rate=interest_rate,
                                                   timeframe=timeframe,
                                                   method_of_repayment=method_of_repayment,
                                                   late_payment_info=late_payment_info)

    def __process_partnership_agreement_document(self):
        summary = self.__generate_summary()
        responsibilities = self.process_prompt("What are the responsibilities of the partners?")
        restrictions = self.process_prompt("What are the restriction on partners")
        dispute_resolution = self.process_prompt("What will disputes be resolved")
        return PartnershipAgreementDocumentResponseSchema(summary=summary,
                                                          responsibilities=responsibilities,
                                                          restrictions=restrictions,
                                                          dispute_resolution=dispute_resolution)