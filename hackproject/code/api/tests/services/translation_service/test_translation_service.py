from unittest.mock import call, Mock

from hackproject.code.api.app.enums import Language
from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponse
from hackproject.code.api.app.services.translation_service.translation_service import TranslationServiceImpl


class TestTranslationService:
    def setup_method(self):
        self.__schema = InsuranceDocumentResponse(
            summary="summary_value",
            included_in_cover = "included_in_cover_value",
            excluded_from_cover = "excluded_from_cover_value",
            emergency_information = "emergency_information_value"
        )

    def test_schema_is_translated(self, mocker):
        mock_return_value = Mock()
        mock_return_value.text.return_value = "test_return_value"
        mock_translate_func = mocker.patch('googletrans.Translator.translate', return_value=mock_return_value)
        translation_service = TranslationServiceImpl()
        translation_service.translate(schema=self.__schema, language=Language.GERMAN)
        expected_calls = [call("summary_value", dest=Language.GERMAN.value),
                          call("included_in_cover_value", dest=Language.GERMAN.value),
                          call("excluded_from_cover_value", dest=Language.GERMAN.value),
                          call("emergency_information_value", dest=Language.GERMAN.value)]
        mock_translate_func.assert_has_calls(expected_calls, any_order=True)
        assert self.__schema.summary == mock_return_value.text
        assert self.__schema.included_in_cover == mock_return_value.text
        assert self.__schema.excluded_from_cover == mock_return_value.text
        assert self.__schema.emergency_information == mock_return_value.text