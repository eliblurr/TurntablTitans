from abc import abstractmethod
from typing import List

from llama_index import GPTSimpleVectorIndex
from llama_index.indices.base import BaseGPTIndex

from hackproject.code.api.app.enums import Document, Prompts, Language
from hackproject.code.api.app.schemas.chat_service.chat_service_schemas import IndexInformation
from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponse, \
    LandDocumentResponse, ServiceContractDocumentResponse, EmploymentContractDocumentResponse, \
    ConfidentialityAgreementDocumentResponse, SalesContractDocumentResponse, \
    IndependentContractorAgreementDocumentResponse, LoanAgreementDocumentResponse, \
    PartnershipAgreementDocumentResponse, PromptResponse
from hackproject.code.api.app.services.translation_service.translation_service import TranslationServiceImpl


class ModelService:
    @abstractmethod
    def get_index(self, document: List):
        pass

    @abstractmethod
    def add_document_to_index(self, index: BaseGPTIndex, document: List):
        pass

    @abstractmethod
    def process_document(self, index_information: IndexInformation, doc_type: Document):
        pass

    @abstractmethod
    def process_prompt(self, prompt: str, index_information: IndexInformation):
        pass

class ModelServiceImpl(ModelService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__translation_service = TranslationServiceImpl()

    def get_index(self, document: List):
        from hackproject.code.api.app.main import service_context
        index = GPTSimpleVectorIndex.from_documents(document, service_context=service_context)
        return index

    def add_document_to_index(self, index: BaseGPTIndex, document: List):
        from hackproject.code.api.app.main import service_context
        for doc in document:
            index.insert(document=doc, service_context=service_context)

    def process_document(self, index_information: IndexInformation, doc_type: Document):
        match doc_type:
            case Document.INSURANCE:
                return self.__process_insurance_document(index_information=index_information)
            case Document.LAND:
                return self.__process_land_document(index_information=index_information)
            case Document.SERVICE_CONTRACT:
                return self.__process_service_contract_document(index_information=index_information)
            case Document.EMPLOYMENT_CONTRACT:
                return self.__process_employment_contract_document(index_information=index_information)
            case Document.CONFIDENTIALITY_AGREEMENT:
                return self.__process_confidentiality_agreement_document(index_information=index_information)
            case Document.SALES_CONTRACT:
                return self.__process_sales_contract_document(index_information=index_information)
            case Document.INDEPENDENT_CONTRACTOR_AGREEMENT:
                return self.__process_independent_contractor_agreement_document(index_information=index_information)
            case Document.LOAN_AGREEMENT:
                return self.__process_loan_agreement_document(index_information=index_information)
            case Document.PARTNERSHIP_AGREEMENT:
                return self.__process_partnership_agreement_document(index_information=index_information)

    def process_prompt(self, prompt: str, index_information: IndexInformation):
        index, language = index_information.index, index_information.language
        return PromptResponse(prompt=prompt, response=index.query(self.__translation_service.translate_text(text=prompt,
                                                                                                     language=language)).response)

    def __generate_summary(self, index_information):
        index = index_information.index
        language = index_information.language
        return index.query(self.__translation_service.translate_text(text=Prompts.SUMMARY.value, language=language)).response

    def __process_insurance_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.INSURANCE.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return InsuranceDocumentResponse(Summary=summary, **answers)

    def __process_land_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.LAND.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return LandDocumentResponse(Summary=summary, **answers)

    def __process_service_contract_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.SERVICE_CONTRACT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return ServiceContractDocumentResponse(Summary=summary, **answers)

    def __process_employment_contract_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.EMPLOYMENT_CONTRACT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return EmploymentContractDocumentResponse(Summary=summary, **answers)

    def __process_confidentiality_agreement_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.CONFIDENTIALITY_AGREEMENT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return ConfidentialityAgreementDocumentResponse(Summary=summary, **answers)

    def __process_sales_contract_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.SALES_CONTRACT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return SalesContractDocumentResponse(Summary=summary, **answers)

    def __process_independent_contractor_agreement_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.INDEPENDENT_CONTRACTOR_AGREEMENT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return IndependentContractorAgreementDocumentResponse(Summary=summary, **answers)

    def __process_loan_agreement_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.LOAN_AGREEMENT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return LoanAgreementDocumentResponse(Summary=summary, **answers)

    def __process_partnership_agreement_document(self, index_information):
        summary = self.__generate_summary(index_information=index_information)
        prompts: dict = Prompts.value_of(Document.PARTNERSHIP_AGREEMENT.value).value
        index = index_information.index
        language = index_information.language
        answers = {k: index.query(self.__translation_service.translate_text(text=v, language=language)).response for k,v in
                   prompts.items()}
        return PartnershipAgreementDocumentResponse(Summary=summary, **answers)