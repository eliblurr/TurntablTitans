import os.path
from unittest.mock import call, Mock

from llama_index import SimpleDirectoryReader

from hackproject.code.api.app.enums import Document, Prompts
from hackproject.code.api.app.services.model_service.model_service import ModelServiceImpl

class TestModelService:
    def setup_method(self):
        test_document_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_document.pdf')
        self.__document = SimpleDirectoryReader(input_files=[test_document_path]).load_data()

    def test_model_is_queried_with_necessary_prompts_for_insurance_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.INSURANCE)
        prompts: dict = Prompts.value_of(Document.INSURANCE.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)


    def test_model_is_queried_with_necessary_prompts_for_land_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.LAND)
        prompts: dict = Prompts.value_of(Document.LAND.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_service_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.SERVICE_CONTRACT)
        prompts: dict = Prompts.value_of(Document.SERVICE_CONTRACT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_employment_contract_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.EMPLOYMENT_CONTRACT)
        prompts: dict = Prompts.value_of(Document.EMPLOYMENT_CONTRACT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_confidentiality_agreement_contract_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.CONFIDENTIALITY_AGREEMENT)
        prompts: dict = Prompts.value_of(Document.CONFIDENTIALITY_AGREEMENT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_sales_contract_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.SALES_CONTRACT)
        prompts: dict = Prompts.value_of(Document.SALES_CONTRACT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_independent_contractor_agreement_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.INDEPENDENT_CONTRACTOR_AGREEMENT)
        prompts: dict = Prompts.value_of(Document.INDEPENDENT_CONTRACTOR_AGREEMENT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_loan_agreement_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.LOAN_AGREEMENT)
        prompts: dict = Prompts.value_of(Document.LOAN_AGREEMENT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)

    def test_model_is_queried_with_necessary_prompts_for_partnership_agreement_document(self, mocker):
        mock_index = Mock()
        mock_index_creator = mocker.patch('llama_index.indices.base.BaseGPTIndex.from_documents',
                                          return_value=mock_index)
        mocker.patch('pydantic.main.BaseModel.__init__', return_value=None)
        model_service = ModelServiceImpl(document=self.__document, type=Document.PARTNERSHIP_AGREEMENT)
        prompts: dict = Prompts.value_of(Document.PARTNERSHIP_AGREEMENT.value).value
        calls = [call(v) for v in prompts.values()]
        calls.append(call(Prompts.SUMMARY.value))
        model_service.process_document()
        mock_index.query.assert_has_calls(calls, any_order=True)
        mock_index_creator.assert_called_with(self.__document)