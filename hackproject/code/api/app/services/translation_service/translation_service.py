from abc import abstractmethod

from googletrans import Translator
from pydantic import BaseModel

from hackproject.code.api.app.enums import Language


class TranslationService:
    @abstractmethod
    def translate(self, schema: BaseModel, language: Language):
        pass

class TranslationServiceImpl(TranslationService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def translate(self, schema: BaseModel, language: Language):
        from hackproject.code.api.app.main import translator
        for field_name in schema.__fields__.keys():
            try:
                translation = translator.translate(getattr(schema, field_name), dest=language.value)
                setattr(schema, field_name, translation.text)
            except:
                continue

        return schema