from abc import abstractmethod

from hackproject.code.api.app.enums import Language
from googletrans import Translator

from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponse, \
    LandDocumentResponse, ServiceContractDocumentResponse, EmploymentContractDocumentResponse, \
    ConfidentialityAgreementDocumentResponse, SalesContractDocumentResponse, \
    IndependentContractorAgreementDocumentResponse, LoanAgreementDocumentResponse, \
    PartnershipAgreementDocumentResponse


class TranslationService:
    @abstractmethod
    def translate(self, schema: InsuranceDocumentResponse |
                                LandDocumentResponse |
                                ServiceContractDocumentResponse |
                                EmploymentContractDocumentResponse |
                                ConfidentialityAgreementDocumentResponse |
                                SalesContractDocumentResponse |
                                IndependentContractorAgreementDocumentResponse |
                                LoanAgreementDocumentResponse |
                                PartnershipAgreementDocumentResponse,
                  language: Language):
        pass

class TranslationServiceImpl(TranslationService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def translate(self, schema: InsuranceDocumentResponse |
                                LandDocumentResponse |
                                ServiceContractDocumentResponse |
                                EmploymentContractDocumentResponse |
                                ConfidentialityAgreementDocumentResponse |
                                SalesContractDocumentResponse |
                                IndependentContractorAgreementDocumentResponse |
                                LoanAgreementDocumentResponse |
                                PartnershipAgreementDocumentResponse,
                  language: Language):
        translator = Translator()
        for field_name in schema.__fields__.keys():
            try:
                translation = translator.translate(getattr(schema, field_name), dest=language.value)
                setattr(schema, field_name, translation.text)
            except:
                continue

        return schema