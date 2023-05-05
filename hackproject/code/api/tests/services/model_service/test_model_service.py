import os.path
from unittest import mock
from unittest.mock import call, Mock

import pytest
from PyPDF2 import PdfReader
from llama_index import Document as LIDocument, ServiceContext
from hackproject.code.api.app.enums import Document, Prompts
from hackproject.code.api.app.services.model_service.model_service import ModelServiceImpl


class TestModelService:
    @pytest.fixture(scope='session', autouse=True)
    def documents(self):
        test_document_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_document.pdf')
        reader = PdfReader(test_document_path)
        pages = reader.pages
        return [LIDocument(page.extract_text()) for page in pages]

    @pytest.fixture(scope='session', autouse=True)
    def mock_service_context(self):
        with mock.patch.object(ServiceContext, 'from_defaults') as _fixture:
            yield _fixture

    def test_new_document_can_be_added_to_existing_index(self, documents, mock_service_context):
        mock_service_context = mock_service_context
        mock_index = Mock()
        model_service = ModelServiceImpl()
        model_service.add_document_to_index(index=mock_index, document=documents)
        calls = [call(document=doc, service_context=mock_service_context()) for doc in documents]
        mock_index.insert.assert_has_calls(calls=calls, any_order=True)

    def test_index_is_built(self, mocker, documents, mock_service_context):
        mock_service_context = mock_service_context
        mock_index_creator = mocker.patch('llama_index.indices.vector_store.vector_indices.GPTSimpleVectorIndex.from_documents')
        model_service = ModelServiceImpl()
        model_service.get_index(documents)
        mock_index_creator.assert_called_with(documents, service_context=mock_service_context())

    def test_index_can_process_prompt(self, mocker):
        mock_index = Mock()
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl()
        prompt = "What is covered under the insurance?"
        model_service.process_prompt(prompt, mock_index)
        mock_index.query.assert_called_with(prompt)

    def test_model_is_queried_with_necessary_prompts_for_type_of_document(self, mocker):
        mock_index = Mock()
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl()
        for document in Document:
            prompts: dict = Prompts.value_of(document.value).value
            calls = [call(v) for v in prompts.values()]
            calls.append(call(Prompts.SUMMARY.value))
            model_service.process_document(mock_index, document)
            mock_index.query.assert_has_calls(calls=calls, any_order=True)