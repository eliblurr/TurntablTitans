from abc import abstractmethod

from googletrans import Translator
from pydantic import BaseModel

from hackproject.code.api.app.enums import Language


class TranslationService:
    @abstractmethod
    def translate_response(self, schema: BaseModel, language: Language):
        pass

    @abstractmethod
    def translate_text(self, text: str, language: Language):
        pass

    @abstractmethod
    def detect_language(self, text: str):
        pass


class TranslationServiceImpl(TranslationService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__translator = Translator()

    def translate_response(self, schema: BaseModel, language: Language):
        for field_name in schema.__fields__.keys():
            try:
                translation = self.__translator.translate(getattr(schema, field_name), dest=language.value)
                setattr(schema, field_name, translation.text)
            except:
                continue

        return schema

    def translate_text(self, text: str, language: Language):
        try:
            translation = self.__translator.translate(text, dest=language.value)
            text = translation.text
        except:
            pass

        return text

    def detect_language(self, text: str):
        try:
            return self.__translator.detect(text).lang
        except:
            pass