import os.path
from unittest.mock import call

from llama_index import SimpleDirectoryReader

from hackproject.code.api.app.enums import Document
from hackproject.code.api.app.services.model_service.model_service import ModelServiceImpl

class TestModelService:
    def setup_method(self):
        test_document_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_document.pdf')
        document = SimpleDirectoryReader(input_files=[test_document_path]).load_data()
        self.__service = ModelServiceImpl(document=document, type=Document.INSURANCE)

    def test_model_is_queried_with_necessary_prompts_for_insurance_document(self, mocker):
        calls = [call("What is included in the cover?"), call("What is excluded from the cover?"),
                   call("Who should I contact in case of emergency?")]
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        mock_prompt_function = mocker.patch('llama_index.indices.base.BaseGPTIndex.query')
        self.__service.process_document()
        mock_prompt_function.assert_has_calls(calls, any_order=True)