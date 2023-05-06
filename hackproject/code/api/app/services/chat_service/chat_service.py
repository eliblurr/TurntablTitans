import random
import time
from abc import abstractmethod

from pydantic import BaseModel

from hackproject.code.api.app.enums import Product, Prompts, Language
from hackproject.code.api.app.schemas.chat_service.chat_service_schemas import IndexInformation
from hackproject.code.api.app.schemas.model_service.model_service_schemas import PromptResponse
from hackproject.code.api.app.schemas.prompt_service.prompt_service_schema import ProcessedPrompt, ChatInitialization
from hackproject.code.api.app.services.model_service.model_service import ModelServiceImpl
from hackproject.code.api.app.services.translation_service.translation_service import TranslationServiceImpl


class ChatService:
    @abstractmethod
    def initialize(self, initialization_details: ChatInitialization):
        pass

    @abstractmethod
    def reply_prompt(self, processed_prompt: ProcessedPrompt):
        pass

class ChatServiceImpl(ChatService):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__translation_service = TranslationServiceImpl()
        self.__model_service = ModelServiceImpl()
        self.__chats = {}

    def initialize(self, initialization_details: ChatInitialization):
        chat_id = initialization_details.chat_id
        self.__chats[chat_id] = None
        if initialization_details.product == Product.MESSAGING:
            bot = self.__get_bot()
            greeting = random.choice(Prompts.GREETING_RESPONSE.value)
            time.sleep(1)
            bot.send_message(chat_id=chat_id, text=greeting)
        else:
            return random.choice(Prompts.GREETING_RESPONSE.value)

    def reply_prompt(self, processed_prompt: ProcessedPrompt):
        if processed_prompt.text:
            return self.__process_text_input(processed_prompt)
        else:
            return self.__process_document_input(processed_prompt)

    def __clean_response(self, schema):
        na_responses = ["I don't know about that, please provide more context",
                        "I am not sure, please provide more context"]

        if isinstance(schema, BaseModel):
            for field_name in schema.__fields__.keys():
                if not getattr(schema, field_name):
                    setattr(schema, field_name, random.choice(na_responses))
        return schema

    def __process_text_input(self, input: ProcessedPrompt):
        def check_pleasantries(formatted_text):
            res = None
            if input.native_language != Language.ENGLISH:
                formatted_text = self.__translation_service.translate_text(formatted_text, Language.ENGLISH)
            if formatted_text in Prompts.GREETING.value or formatted_text+'?' in Prompts.GREETING.value:
                res = PromptResponse(prompt=input.text,
                                     response=random.choice(Prompts.GREETING_RESPONSE.value))
            elif formatted_text in Prompts.APPRECIATION.value:
                res = PromptResponse(prompt=input.text, response=random.choice(Prompts.APPRECIATION_RESPONSE.value))
            return res

        ## check if input is a pleasantry
        response = check_pleasantries(input.text.lower().strip())

        if not response:
            if not self.__chats.get(input.chat_id):
                response = PromptResponse(prompt=input.text,
                                              response=Prompts.NO_DOCUMENT_PROVIDED_REPLY.value)
            else:
                index_information: IndexInformation = self.__chats.get(input.chat_id)
                response = self.__model_service.process_prompt(prompt=input.text, index_information=index_information)

        response = self.__clean_response(response)
        response = self.__translation_service.translate_response(schema=response, language=input.native_language)
        if input.product == Product.WEB:
            return response
        else:
            bot = self.__get_bot()
            bot.send_message(chat_id=input.chat_id, text=response.response)

    def __process_document_input(self, input: ProcessedPrompt):
        def process():
            index_information = self.__chats.get(input.chat_id)
            if not index_information:
                index = self.__model_service.get_index(document=input.document.document)
                language = input.document.doc_language
                self.__chats[input.chat_id] = IndexInformation(index=index, language=language)
                index_information = self.__chats.get(input.chat_id)
            else:
                self.__model_service.add_document_to_index(index=index_information.index, document=input.document.document)
            response = self.__model_service.process_document(index_information=index_information, doc_type=input.document.doc_type)
            response = self.__clean_response(response)
            return self.__translation_service.translate_response(schema=response, language=input.native_language)

        if input.product == Product.WEB:
            return process()
        else:
            translated_response = process()
            if isinstance(translated_response, BaseModel):
                for field_name in translated_response.__fields__.keys():
                    bot = self.__get_bot()
                    bot.send_message(input.chat_id, getattr(translated_response, field_name))

    def __get_bot(self):
        from hackproject.code.api.app.main import bot
        return bot