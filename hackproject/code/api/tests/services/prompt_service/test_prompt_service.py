import os

import pytest
from fastapi import HTTPException

from hackproject.code.api.app.enums import Document, Product, Language
from hackproject.code.api.app.schemas.prompt_service.prompt_service_schema import WebDocument, WebPrompt, WebText
from hackproject.code.api.app.services.prompt_service.prompt_service import PromptServiceImpl


class TestPromptService:

    def test_exception_is_thrown_if_no_native_language_given(self):
        body = "this is a prompt"
        native_language = "UNSUPPORTED_LANGUAGE"
        chat_id = "chat_id"
        text = WebText(body=body, native_language=native_language)
        prompt = WebPrompt(prompt=text, chat_id=chat_id)

        ps = PromptServiceImpl()
        with pytest.raises(HTTPException):
            ps.process_prompt(prompt)

    def test_exception_is_thrown_if_file_does_not_exist_for_document_prompts(self, mocker):
        type = Document.INSURANCE
        doc_language = "ENGLISH"
        file_path = "some/path"
        native_language = "FRENCH"
        chat_id = "chat_id"
        document = WebDocument(type=type, doc_language=doc_language, file_path=file_path,
                               native_language=native_language)
        prompt =  WebPrompt(prompt=document, chat_id=chat_id)

        ps = PromptServiceImpl()
        with pytest.raises(HTTPException):
            ps.process_prompt(prompt)

    def test_exception_is_thrown_if_document_in_unsupported_language(self):
        type = Document.INSURANCE
        doc_language = "ENGLISH"
        test_document_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_document.pdf')
        native_language = "UNSUPPORTED_LANGUAGE"
        chat_id = "chat_id"
        document = WebDocument(type=type, doc_language=doc_language, file_path=test_document_path,
                               native_language=native_language)
        prompt =  WebPrompt(prompt=document, chat_id=chat_id)

        ps = PromptServiceImpl()
        with pytest.raises(HTTPException):
            ps.process_prompt(prompt)

    def test_document_prompt_is_processed(self):
        type = Document.INSURANCE
        doc_language = "ENGLISH"
        test_document_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_document.pdf')
        native_language = "FRENCH"
        chat_id = "chat_id"
        document = WebDocument(type=type, doc_language=doc_language, file_path=test_document_path,
                               native_language=native_language)
        prompt = WebPrompt(prompt=document, chat_id=chat_id)

        ps = PromptServiceImpl()
        processed_prompt = ps.process_prompt(prompt)
        assert processed_prompt.chat_id == chat_id
        assert processed_prompt.native_language == Language.FRENCH
        assert processed_prompt.product == Product.WEB
        assert processed_prompt.document.doc_type == type
        assert processed_prompt.document.doc_language == Language.ENGLISH

    def test_text_prompt_is_processed(self):
        body = "this is a prompt"
        native_language = "FRENCH"
        chat_id = "chat_id"
        text = WebText(body=body, native_language=native_language)
        prompt = WebPrompt(prompt=text, chat_id=chat_id)

        ps = PromptServiceImpl()
        processed_prompt = ps.process_prompt(prompt)
        assert processed_prompt.chat_id == chat_id
        assert processed_prompt.native_language == Language.FRENCH
        assert processed_prompt.product == Product.WEB
        assert processed_prompt.text == body