import datetime
import os.path
import time
from abc import abstractmethod

from PyPDF2 import PdfReader
from fastapi import HTTPException
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index import Document as LIDocument, SimpleDirectoryReader
from telebot import types

from hackproject.code.api.app.enums import Language, Document, Product
from hackproject.code.api.app.schemas.prompt_service.prompt_service_schema import WebPrompt, WebDocument, \
    ProcessedPrompt, ProcessedDocument
from telegram.ext import ConversationHandler


class PromptService:
    @abstractmethod
    def process_prompt(self, body: WebPrompt | types.Message):
        pass

class PromptServiceImpl(PromptService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def process_prompt(self, body: WebPrompt | types.Message):
        if isinstance(body, types.Message):
            return self.messaging_prompt(body)
        else:
            return self.web_prompt(body)


    def __sanitize_prompt(self, prompt: str):
        ## remove malicious prompts
        return prompt

    def web_prompt(self, body: WebPrompt):
        destination_language: Language = Language.value_of(body.type.language)
        if isinstance(body.type, WebDocument):
            if os.path.exists(body.type.file_path):
                document = self.__load_document(body.type.file_path)
            else:
                raise HTTPException(status_code=400, detail="Bad request")

            processed_document: ProcessedDocument = ProcessedDocument(
                document = document,
                doc_type = body.type.type
            )

            return ProcessedPrompt(chat_id=body.chat_id, document=processed_document, language=destination_language,
                                   product=Product.WEB)
        else:
            text = self.__sanitize_prompt(body.type.body)

            return ProcessedPrompt(chat_id=body.chat_id, text=text, language=destination_language, product=Product.WEB)

    def messaging_prompt(self, message):
        if message.content_type == 'text':
            return ProcessedPrompt(chat_id=message.chat.id, text=message.text, language=Language.ENGLISH, product=Product.MESSAGING)
        else:
            details = {}
            self.handle_file(message, details)
            start_time = datetime.datetime.now()
            while len(details) < 3 and (datetime.datetime.now() - start_time).total_seconds()/60 < 2:
                pass

            ## if too much time has passed
            if len(details) < 3: return

            downloaded_file_path, doc_type, language = details["downloaded_file_path"], details["doc_type"], details["language"]
            document = self.__load_document(downloaded_file_path)
            os.remove(downloaded_file_path)
            processed_document: ProcessedDocument = ProcessedDocument(
                document=document,
                doc_type=Document.value_of(doc_type.replace(" ", "_"))
            )
            return ProcessedPrompt(chat_id=message.chat.id,
                                   document=processed_document,
                                   language=Language.value_of(language.replace(" ", "_")),
                                   product=Product.MESSAGING)

    def handle_file(self, message, details):
        bot = self.__get_bot()
        bot.send_chat_action(chat_id=message.chat.id, action='typing')
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = file_info.file_path.split("/")[-1]
        save_file_path = os.path.join(dir_path, "downloads", file_name)
        with open(save_file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        details["downloaded_file_path"] = save_file_path

        self.__ask_document_type(message, details)

    def __ask_document_type(self, message, details):
        bot = self.__get_bot()
        bot.send_chat_action(chat_id=message.chat.id, action='typing')

        options = [doc.name.split(".")[-1].replace("_", " ") for doc in Document]
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for option in options:
            button = types.KeyboardButton(text=option)
            keyboard.add(button)

        time.sleep(1)
        msg = bot.reply_to(message, 'What type of document is it?', reply_markup=keyboard)

        bot.register_next_step_handler(msg, self.__ask_language, details)

    def __ask_language(self, message, details):
        bot = self.__get_bot()
        bot.send_chat_action(chat_id=message.chat.id, action='typing')

        option = message.text
        details["doc_type"] = option
        bot.reply_to(message, f"You selected: {option}", reply_markup=types.ReplyKeyboardRemove())
        text = "Awesome!, select the language you want to interact with the document in."
        options = [language.name.replace("_", " ") for language in Language]

        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for option in options:
            button = types.KeyboardButton(text=option)
            keyboard.add(button)

        time.sleep(1)
        msg = bot.reply_to(message, text, reply_markup=keyboard)

        bot.register_next_step_handler(msg, self.__receive_language, details)

    def __receive_language(self, message, details):
        bot = self.__get_bot()
        bot.send_chat_action(chat_id=message.chat.id, action='typing')
        option = message.text
        details["language"] = option
        bot.reply_to(message, f"You selected: {option}", reply_markup=types.ReplyKeyboardRemove())
        bot.reply_to(message, "Awesome!, hold on while I read your document.")
        return ConversationHandler.END

    def __get_bot(self):
        from hackproject.code.api.app.main import bot
        return bot

    def __load_document(self, path: str):
        reader = PdfReader(path)
        pages = reader.pages
        return [LIDocument(page.extract_text()) for page in pages]