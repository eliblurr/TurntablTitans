import os
from abc import abstractmethod
from llama_index import GPTSimpleVectorIndex
from hackproject.code.api.app.enums import Document
from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponseSchema, \
    LandDocumentResponseSchema, ServiceContractDocumentResponseSchema, EmploymentContractDocumentResponseSchema
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
        return self.__index.query(prompt)

    def __process_insurance_document(self):
        summary = self.__generate_summary()
        included_in_cover = self.process_prompt("What is included in the cover?")
        excluded_from_cover = self.process_prompt("What is excluded from the cover?")
        emergency_information = self.process_prompt("Who should I contact in case of emergency?")
        return InsuranceDocumentResponseSchema(summary=summary.response, included_in_cover=included_in_cover.response,
                                               excluded_from_cover=excluded_from_cover.response,
                                               emergency_information=emergency_information.response)

    def __process_land_document(self):
        summary = self.__generate_summary()
        description = self.process_prompt("Describe the property briefly")
        terms_of_use = self.process_prompt("What are the terms of use?")
        warranties_and_guarantees = self.process_prompt("What are the warranties and guarantees")
        return LandDocumentResponseSchema(summary=summary.response, description=description.response,
                                               terms_of_use=terms_of_use.response,
                                               warranties_and_guarantees=warranties_and_guarantees.response)

    def __process_service_contract_document(self):
        summary = self.__generate_summary()
        payment_and_services = self.process_prompt("How and what exactly is the vendor being paid for its services?")
        obligations = self.process_prompt("What are my obligations?")
        liability = self.process_prompt("How will be responsible for mistakes?")
        return ServiceContractDocumentResponseSchema(summary=summary.response, payment_and_services=payment_and_services.response,
                                          obligations=obligations.response,
                                          liability=liability.response)

    def __process_employment_contract_document(self):
        summary = self.__generate_summary()
        start_date = self.process_prompt("What is the start date?")
        benefits_and_packages = self.process_prompt("What are the benefits and packages")
        schedule = self.process_prompt("Is there a defined schedule?")
        response_deadline = self.process_prompt("Am I expected to give my answer before a certain date?")
        return EmploymentContractDocumentResponseSchema(summary=summary.response,
                                                     start_date=start_date.response,
                                                     benefits_and_packages=benefits_and_packages.response,
                                                     schedule=schedule.response,
                                                     response_deadline=response_deadline.response)

    def __process_confidentiality_agreement_document(self):
        pass

    def __process_sales_contract_document(self):
        pass

    def __process_independent_contractor_agreement_document(self):
        pass

    def __process_loan_agreement_document(self):
        pass

    def __process_partnership_agreement_document(self):
        pass