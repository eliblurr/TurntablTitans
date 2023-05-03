import random
import time
from abc import abstractmethod

from hackproject.code.api.app.enums import Product, Prompts
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
        responses = ["Initializing..."]
        chat_id = initialization_details.chat_id
        self.__chats[chat_id] = None
        if initialization_details.product == Product.MESSAGING:
            bot = self.__get_bot()
            bot.send_message(chat_id, responses[0])
            # give time to read what has been printed
            time.sleep(1)
            # Greet and introduce
            greeting = random.choice(Prompts.GREETING_RESPONSE.value)
            bot.send_message(chat_id, greeting)
        else:
            return [responses[0], random.choice(Prompts.GREETING_RESPONSE.value)]

    def reply_prompt(self, processed_prompt: ProcessedPrompt):
        if processed_prompt.text:
            return self.__process_text_input(processed_prompt)
        else:
            return self.__process_document_input(processed_prompt)

    def __clean_response(self, schema):
        na_responses = ["I don't know about that, please provide more context",
                        "I am not sure, please provide more context"]

        for field_name in schema.__fields__.keys():
            if not getattr(schema, field_name):
                setattr(schema, field_name, random.choice(na_responses))
        return schema

    def __process_text_input(self, input: ProcessedPrompt):
        def check_pleasantries(formatted_text):
            res = None
            if formatted_text in Prompts.GREETING.value or formatted_text+'?' in Prompts.GREETING.value:
                res = PromptResponse(prompt=input.text, response=random.choice(Prompts.GREETING_RESPONSE.value))
            elif formatted_text in ['thanks', 'thank you', 'appreciate it',
                                      'grateful', 'cheers', 'nice one', 'alright', 'cool'
                                      'bye', 'exit', 'quit', 'ok', 'okay'] :
                res = PromptResponse(prompt=input.text, response="Happy to help!")
            return res

        ## check if input is a pleasantry
        response = check_pleasantries(input.text.lower().strip())

        if not response:
            if not self.__chats.get(input.chat_id):
                response = PromptResponse(prompt=input.text,
                                              response="I need a document first before I can answer questions")
            else:
                response = self.__model_service.process_prompt(prompt=input.text, index=self.__chats.get(input.chat_id))

        response = self.__clean_response(response)
        response = self.__translation_service.translate(schema=response, language=input.language)
        if input.product == Product.WEB:
            return response
        else:
            bot = self.__get_bot()
            bot.send_message(input.chat_id, response.response)

    def __process_document_input(self, input: ProcessedPrompt):
        def process():
            index = self.__chats.get(input.chat_id)
            if not self.__chats.get(input.chat_id):
                self.__chats[input.chat_id] = self.__model_service.get_index(document=input.document.document)
                index = self.__chats.get(input.chat_id)
            else:
                self.__model_service.add_document_to_index(index=index, document=input.document.document)
            response = self.__model_service.process_document(index=index, doc_type=input.document.doc_type)
            return self.__translation_service.translate(schema=response, language=input.language)

        if input.product == Product.WEB:
            return process()
        else:
            translated_response = process()
            for field_name in translated_response.__fields__.keys():
                bot = self.__get_bot()
                bot.send_message(input.chat_id, getattr(translated_response, field_name))

    def __get_bot(self):
        from hackproject.code.api.app.main import bot
        return bot