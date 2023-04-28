import os
from abc import abstractmethod
from typing import List

from llama_index import GPTSimpleVectorIndex
from hackproject.code.api.app.enums import Document, Prompts
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
    def __init__(self, document: List, type: Document, openai_api_key=None):
        if not openai_api_key:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            env_path = os.path.join(dir_path, '..', '..', '.env')
            config = dotenv_values(env_path)
            openai_api_key = config.get('OPENAI_API_KEY')
            if openai_api_key:
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
        return self.process_prompt(Prompts.SUMMARY.value)

    def process_prompt(self, prompt: str):
        return self.__index.query(prompt).response

    def __process_insurance_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.INSURANCE.value).value
        answers = {k: self.process_prompt(v) for k,v in prompts.items()}
        return InsuranceDocumentResponseSchema(summary=summary, **answers)

    def __process_land_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.LAND.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return LandDocumentResponseSchema(summary=summary, **answers)

    def __process_service_contract_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.SERVICE_CONTRACT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return ServiceContractDocumentResponseSchema(summary=summary, **answers)

    def __process_employment_contract_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.EMPLOYMENT_CONTRACT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return EmploymentContractDocumentResponseSchema(summary=summary, **answers)

    def __process_confidentiality_agreement_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.CONFIDENTIALITY_AGREEMENT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return ConfidentialityAgreementDocumentResponseSchema(summary=summary, **answers)

    def __process_sales_contract_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.SALES_CONTRACT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return SalesContractDocumentResponseSchema(summary=summary, **answers)

    def __process_independent_contractor_agreement_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.INDEPENDENT_CONTRACTOR_AGREEMENT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return IndependentContractorAgreementDocumentResponseSchema(summary=summary, **answers)

    def __process_loan_agreement_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.LOAN_AGREEMENT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return LoanAgreementDocumentResponseSchema(summary=summary, **answers)

    def __process_partnership_agreement_document(self):
        summary = self.__generate_summary()
        prompts: dict = Prompts.value_of(Document.PARTNERSHIP_AGREEMENT.value).value
        answers = {k: self.process_prompt(v) for k, v in prompts.items()}
        return PartnershipAgreementDocumentResponseSchema(summary=summary, **answers)