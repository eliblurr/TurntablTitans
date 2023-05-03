from abc import abstractmethod
from typing import List

from llama_index import GPTSimpleVectorIndex
from llama_index.indices.base import BaseGPTIndex

from hackproject.code.api.app.enums import Document, Prompts
from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponse, \
    LandDocumentResponse, ServiceContractDocumentResponse, EmploymentContractDocumentResponse, \
    ConfidentialityAgreementDocumentResponse, SalesContractDocumentResponse, \
    IndependentContractorAgreementDocumentResponse, LoanAgreementDocumentResponse, \
    PartnershipAgreementDocumentResponse, PromptResponse


class ModelService:
    @abstractmethod
    def get_index(self, document: List):
        pass

    @abstractmethod
    def add_document_to_index(self, index: BaseGPTIndex, document: List):
        pass

    @abstractmethod
    def process_document(self, index: BaseGPTIndex, doc_type: Document):
        pass

    @abstractmethod
    def process_prompt(self, prompt: str, index: BaseGPTIndex):
        pass

class ModelServiceImpl(ModelService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_index(self, document: List):
        from hackproject.code.api.app.main import service_context
        index = GPTSimpleVectorIndex.from_documents(document, service_context=service_context)
        return index

    def add_document_to_index(self, index: BaseGPTIndex, document: List):
        from hackproject.code.api.app.main import service_context
        for doc in document:
            index.insert(document=doc, service_context=service_context)

    def process_document(self, index: BaseGPTIndex, doc_type: Document):
        match doc_type:
            case Document.INSURANCE:
                return self.__process_insurance_document(index=index)
            case Document.LAND:
                return self.__process_land_document(index=index)
            case Document.SERVICE_CONTRACT:
                return self.__process_service_contract_document(index=index)
            case Document.EMPLOYMENT_CONTRACT:
                return self.__process_employment_contract_document(index=index)
            case Document.CONFIDENTIALITY_AGREEMENT:
                return self.__process_confidentiality_agreement_document(index=index)
            case Document.SALES_CONTRACT:
                return self.__process_sales_contract_document(index=index)
            case Document.INDEPENDENT_CONTRACTOR_AGREEMENT:
                return self.__process_independent_contractor_agreement_document(index=index)
            case Document.LOAN_AGREEMENT:
                return self.__process_loan_agreement_document(index=index)
            case Document.PARTNERSHIP_AGREEMENT:
                return self.__process_partnership_agreement_document(index=index)

    def process_prompt(self, prompt: str, index: BaseGPTIndex):
        return PromptResponse(prompt=prompt, response=index.query(prompt).response)

    def __generate_summary(self, index: BaseGPTIndex):
        return index.query(Prompts.SUMMARY.value).response

    def __process_insurance_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.INSURANCE.value).value
        answers = {k: index.query(v).response for k,v in prompts.items()}
        return InsuranceDocumentResponse(summary=summary, **answers)

    def __process_land_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.LAND.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return LandDocumentResponse(summary=summary, **answers)

    def __process_service_contract_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.SERVICE_CONTRACT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return ServiceContractDocumentResponse(summary=summary, **answers)

    def __process_employment_contract_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.EMPLOYMENT_CONTRACT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return EmploymentContractDocumentResponse(summary=summary, **answers)

    def __process_confidentiality_agreement_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.CONFIDENTIALITY_AGREEMENT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return ConfidentialityAgreementDocumentResponse(summary=summary, **answers)

    def __process_sales_contract_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.SALES_CONTRACT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return SalesContractDocumentResponse(summary=summary, **answers)

    def __process_independent_contractor_agreement_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.INDEPENDENT_CONTRACTOR_AGREEMENT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return IndependentContractorAgreementDocumentResponse(summary=summary, **answers)

    def __process_loan_agreement_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.LOAN_AGREEMENT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return LoanAgreementDocumentResponse(summary=summary, **answers)

    def __process_partnership_agreement_document(self, index: BaseGPTIndex):
        summary = self.__generate_summary(index=index)
        prompts: dict = Prompts.value_of(Document.PARTNERSHIP_AGREEMENT.value).value
        answers = {k: index.query(v).response for k, v in prompts.items()}
        return PartnershipAgreementDocumentResponse(summary=summary, **answers)