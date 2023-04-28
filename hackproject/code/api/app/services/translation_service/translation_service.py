from abc import abstractmethod

from hackproject.code.api.app.enums import Language
from googletrans import Translator

from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponseSchema, \
    LandDocumentResponseSchema, ServiceContractDocumentResponseSchema, EmploymentContractDocumentResponseSchema, \
    ConfidentialityAgreementDocumentResponseSchema, SalesContractDocumentResponseSchema, \
    IndependentContractorAgreementDocumentResponseSchema, LoanAgreementDocumentResponseSchema, \
    PartnershipAgreementDocumentResponseSchema


class TranslationService:
    @abstractmethod
    def translate(self, schema: InsuranceDocumentResponseSchema |
                                LandDocumentResponseSchema |
                                ServiceContractDocumentResponseSchema |
                                EmploymentContractDocumentResponseSchema |
                                ConfidentialityAgreementDocumentResponseSchema |
                                SalesContractDocumentResponseSchema |
                                IndependentContractorAgreementDocumentResponseSchema |
                                LoanAgreementDocumentResponseSchema |
                                PartnershipAgreementDocumentResponseSchema ,
                        language: Language):
        pass

class TranslationServiceImpl(TranslationService):
    def translate(self, schema: InsuranceDocumentResponseSchema |
                                LandDocumentResponseSchema |
                                ServiceContractDocumentResponseSchema |
                                EmploymentContractDocumentResponseSchema |
                                ConfidentialityAgreementDocumentResponseSchema |
                                SalesContractDocumentResponseSchema |
                                IndependentContractorAgreementDocumentResponseSchema |
                                LoanAgreementDocumentResponseSchema |
                                PartnershipAgreementDocumentResponseSchema,
                  language: Language):
        translator = Translator()
        for field_name in schema.__fields__.keys():
            try:
                translation = translator.translate(getattr(schema, field_name), dest=language.value)
                setattr(schema, field_name, translation.text)
            except:
                continue

        return schema