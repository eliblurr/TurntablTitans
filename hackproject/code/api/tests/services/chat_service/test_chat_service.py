import os
import random
from unittest.mock import Mock

import pytest
from PyPDF2 import PdfReader

from hackproject.code.api.app.enums import Prompts, Product, Language, Document
from hackproject.code.api.app.schemas.model_service.model_service_schemas import PromptResponse
from hackproject.code.api.app.schemas.prompt_service.prompt_service_schema import ChatInitialization, ProcessedPrompt, \
    ProcessedDocument
from hackproject.code.api.app.services.chat_service.chat_service import ChatServiceImpl
from llama_index import Document as LIDocument

@pytest.fixture(scope='class', autouse=True)
def mock_bot():
    return Mock()

@pytest.fixture()
def prepare_mocks(mocker):
    mocker.patch("langchain.OpenAI")
    mocker.patch("llama_index.LLMPredictor")
    mocker.patch("langchain.embeddings.huggingface.HuggingFaceEmbeddings")
    mocker.patch("llama_index.LangchainEmbedding")
    mocker.patch("llama_index.indices.service_context.ServiceContext.from_defaults")

@pytest.fixture(scope='class', autouse=True)
def processed_document():
    test_document_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_document.pdf')
    reader = PdfReader(test_document_path)
    pages = reader.pages
    documents = [LIDocument(page.extract_text()) for page in pages]
    doc_types = [doc for doc in Document]
    return ProcessedDocument(document=documents, doc_type=random.choice(doc_types), doc_language=Language.ENGLISH)

@pytest.mark.usefixtures("mock_bot")
@pytest.mark.usefixtures("prepare_mocks")
@pytest.mark.usefixtures("processed_document")
class TestChatService:
    ## general
    def test_text_prompts_are_translated_to_native_language_given(self, mocker):
        chat_id = "chat_id"
        appreciation = random.choice(Prompts.APPRECIATION.value)
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=appreciation, native_language=Language.ENGLISH,
                                                            product=Product.WEB, chat_id=chat_id)
        mock_translation_func = mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        mock_translation_func.assert_called_with(schema=response, language=processed_prompt.native_language)

    def test_document_prompts_are_translated_to_native_language_given(self, mocker, processed_document):
        chat_id = "chat_id"
        document_prompt = ProcessedPrompt(document=processed_document, native_language=Language.FRENCH,
                                          product=Product.WEB, chat_id=chat_id)
        mock_index_information = Mock()
        mocker.patch("hackproject.code.api.app.schemas.chat_service.chat_service_schemas.IndexInformation.__new__",
                     return_value=mock_index_information)
        mock_translation_func = mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        mocker.patch(
            "hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.get_index")
        mocker.patch(
            "hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.process_document")
        cs = ChatServiceImpl()
        mock_response_from_index = "Return value from mock"
        mock_index_information.index.query.return_value.response = mock_response_from_index
        response = cs.reply_prompt(document_prompt)
        mock_translation_func.assert_called_with(schema=response, language=document_prompt.native_language)

    ## web prompts
    def test_web_chat_initialization(self):
        chat_id = "chat_id"
        initialization_info: ChatInitialization = ChatInitialization(product=Product.WEB, chat_id=chat_id)
        cs = ChatServiceImpl()
        response = cs.initialize(initialization_details=initialization_info)
        assert response in Prompts.GREETING_RESPONSE.value

    def test_web_greetings_are_replied(self, mocker):
        chat_id = "chat_id"
        greeting = random.choice(Prompts.GREETING.value)
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=greeting, native_language=Language.ENGLISH,
                                                            product=Product.WEB, chat_id=chat_id)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        assert response.prompt == greeting
        assert response.response in Prompts.GREETING_RESPONSE.value

    def test_web_appreciation_messages_are_replied(self, mocker):
        chat_id = "chat_id"
        appreciation = random.choice(Prompts.APPRECIATION.value)
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=appreciation, native_language=Language.ENGLISH,
                                                            product=Product.WEB, chat_id=chat_id)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        assert response.prompt == appreciation
        assert response.response in Prompts.APPRECIATION_RESPONSE.value

    def test_web_messages_are_replied_appropriately_when_no_document_has_been_provided(self, mocker):
        chat_id = "chat_id"
        prompt = "What is covered by the insurance?"
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=prompt, native_language=Language.ENGLISH,
                                                            product=Product.WEB, chat_id=chat_id)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        assert response.prompt == prompt
        assert response.response == Prompts.NO_DOCUMENT_PROVIDED_REPLY.value

    def test_web_messages_are_replied_using_index_when_document_has_been_provided(self, mocker, processed_document):
        chat_id = "chat_id"
        prompt = "What is covered by the insurance?"
        document_prompt = ProcessedPrompt(document=processed_document, native_language=Language.FRENCH,
                                          product=Product.WEB, chat_id=chat_id)
        text_prompt: ProcessedPrompt = ProcessedPrompt(text=prompt, native_language=Language.ENGLISH,
                                                            product=Product.WEB, chat_id=chat_id)
        mock_index_information = Mock()
        mocker.patch("hackproject.code.api.app.schemas.chat_service.chat_service_schemas.IndexInformation.__new__",
                     return_value=mock_index_information)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.get_index")
        mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.process_document")
        cs = ChatServiceImpl()
        cs.reply_prompt(document_prompt)
        mock_response_from_index = "Return value from mock"
        mock_index_information.index.query.return_value.response = mock_response_from_index
        response: PromptResponse = cs.reply_prompt(text_prompt)
        assert response.prompt == prompt
        assert response.response == mock_response_from_index

    def test_web_index_is_built_from_document_and_processed(self, mocker, processed_document):
        chat_id = "chat_id"
        document_prompt = ProcessedPrompt(document=processed_document, native_language=Language.FRENCH,
                                          product=Product.WEB, chat_id=chat_id)
        mock_index_information = Mock()
        mocker.patch("hackproject.code.api.app.schemas.chat_service.chat_service_schemas.IndexInformation.__new__",
                     return_value=mock_index_information)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        mock_get_index_func = mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.get_index")
        mock_process_document_with_index_func = mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.process_document")
        cs = ChatServiceImpl()
        mock_response_from_index = "Return value from mock"
        mock_index_information.index.query.return_value.response = mock_response_from_index
        response = cs.reply_prompt(document_prompt)
        mock_get_index_func.assert_called_with(document=document_prompt.document.document)
        mock_process_document_with_index_func.assert_called_with(index_information=mock_index_information, doc_type=document_prompt.document.doc_type)
        assert response

    ## mobile prompts
    def test_messaging_chat_initialization(self, mocker, mock_bot, prepare_mocks):
        mocker.patch("telebot.TeleBot", return_value=mock_bot)
        mock_bot.token = "token"
        chat_id = "chat_id"
        initialization_info: ChatInitialization = ChatInitialization(product=Product.MESSAGING, chat_id=chat_id)
        cs = ChatServiceImpl()
        response = cs.initialize(initialization_details=initialization_info)
        args, kwargs = mock_bot.send_message.call_args
        assert kwargs['chat_id'] == chat_id
        assert kwargs['text'] in Prompts.GREETING_RESPONSE.value
        assert not response

    def test_messaging_greetings_are_replied(self, mocker, mock_bot, prepare_mocks):
        mocker.patch("telebot.TeleBot", return_value=mock_bot)
        mock_bot.token = "token"
        chat_id = "chat_id"
        greeting = random.choice(Prompts.GREETING.value)
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=greeting, native_language=Language.ENGLISH,
                                                            product=Product.MESSAGING, chat_id=chat_id)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        args, kwargs = mock_bot.send_message.call_args
        assert kwargs['chat_id'] == chat_id
        assert kwargs['text'] in Prompts.GREETING_RESPONSE.value
        assert not response

    def test_messaging_appreciation_messages_are_replied(self, mocker, mock_bot, prepare_mocks):
        mocker.patch("telebot.TeleBot", return_value=mock_bot)
        mock_bot.token = "token"
        chat_id = "chat_id"
        appreciation = random.choice(Prompts.APPRECIATION.value)
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=appreciation, native_language=Language.ENGLISH,
                                                            product=Product.MESSAGING, chat_id=chat_id)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        args, kwargs = mock_bot.send_message.call_args
        assert kwargs['chat_id'] == chat_id
        assert kwargs['text'] in Prompts.APPRECIATION_RESPONSE.value
        assert not response

    def test_messaging_messages_are_replied_appropriately_when_no_document_has_been_provided(self, mocker,
                                                                                             mock_bot, prepare_mocks):
        mocker.patch("telebot.TeleBot", return_value=mock_bot)
        mock_bot.token = "token"
        chat_id = "chat_id"
        prompt = "What is covered by the insurance?"
        processed_prompt: ProcessedPrompt = ProcessedPrompt(text=prompt, native_language=Language.ENGLISH,
                                                            product=Product.MESSAGING, chat_id=chat_id)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        cs = ChatServiceImpl()
        response: PromptResponse = cs.reply_prompt(processed_prompt)
        args, kwargs = mock_bot.send_message.call_args
        assert kwargs['chat_id'] == chat_id
        assert kwargs['text'] in Prompts.NO_DOCUMENT_PROVIDED_REPLY.value
        assert not response

    def test_messaging_messages_are_replied_using_index_when_document_has_been_provided(self, mocker, mock_bot,
                                                                                       prepare_mocks,
                                                                                       processed_document):
        mocker.patch("telebot.TeleBot", return_value=mock_bot)
        mock_bot.token = "token"
        chat_id = "chat_id"
        prompt = "What is covered by the insurance?"
        document_prompt = ProcessedPrompt(document=processed_document, native_language=Language.FRENCH,
                                          product=Product.MESSAGING, chat_id=chat_id)
        text_prompt: ProcessedPrompt = ProcessedPrompt(text=prompt, native_language=Language.ENGLISH,
                                                            product=Product.MESSAGING, chat_id=chat_id)
        mock_index_information = Mock()
        mocker.patch("hackproject.code.api.app.schemas.chat_service.chat_service_schemas.IndexInformation.__new__",
                     return_value=mock_index_information)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.get_index")
        mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.process_document")
        cs = ChatServiceImpl()
        cs.reply_prompt(document_prompt)
        mock_response_from_index = "Return value from mock"
        mock_index_information.index.query.return_value.response = mock_response_from_index
        response: PromptResponse = cs.reply_prompt(text_prompt)
        args, kwargs = mock_bot.send_message.call_args
        assert kwargs['chat_id'] == chat_id
        assert kwargs['text'] == mock_response_from_index
        assert not response

    def test_mobile_index_is_built_from_document_and_processed(self, mocker, mock_bot, prepare_mocks,
                                                               processed_document):
        mocker.patch("telebot.TeleBot", return_value=mock_bot)
        mock_bot.token = "token"
        chat_id = "chat_id"
        document_prompt = ProcessedPrompt(document=processed_document, native_language=Language.FRENCH,
                                          product=Product.MESSAGING, chat_id=chat_id)
        mock_index_information = Mock()
        mocker.patch("hackproject.code.api.app.schemas.chat_service.chat_service_schemas.IndexInformation.__new__",
                     return_value=mock_index_information)
        mocker.patch("hackproject.code.api.app.services.translation_service.translation_service.TranslationServiceImpl"
                     ".translate_response", side_effect=lambda schema, language: schema)
        mock_get_index_func = mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.get_index")
        mock_process_document_with_index_func = mocker.patch("hackproject.code.api.app.services.model_service.model_service.ModelServiceImpl.process_document")
        cs = ChatServiceImpl()
        mock_response_from_index = "Return value from mock"
        mock_index_information.index.query.return_value.response = mock_response_from_index
        cs.reply_prompt(document_prompt)
        mock_get_index_func.assert_called_with(document=document_prompt.document.document)
        mock_process_document_with_index_func.assert_called_with(index_information=mock_index_information, doc_type=document_prompt.document.doc_type)