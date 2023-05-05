from unittest.mock import call, Mock

import pytest

from hackproject.code.api.app.enums import Language
from hackproject.code.api.app.schemas.model_service.model_service_schemas import InsuranceDocumentResponse
from hackproject.code.api.app.services.translation_service.translation_service import TranslationServiceImpl


class TestTranslationService:
    @pytest.fixture()
    def test_schema(self):
        return InsuranceDocumentResponse(
            summary="summary_value",
            included_in_cover = "included_in_cover_value",
            excluded_from_cover = "excluded_from_cover_value",
            emergency_information = "emergency_information_value")

    def test_schema_is_translated(self, mocker, test_schema):
        mock_translator = Mock()
        mock_translator.text.return_value = "test_return_value"
        mock_translate_func = mocker.patch('googletrans.Translator.translate', return_value=mock_translator)
        translation_service = TranslationServiceImpl()
        translation_service.translate_response(schema=test_schema, language=Language.GERMAN)
        expected_calls = [call("summary_value", dest=Language.GERMAN.value),
                          call("included_in_cover_value", dest=Language.GERMAN.value),
                          call("excluded_from_cover_value", dest=Language.GERMAN.value),
                          call("emergency_information_value", dest=Language.GERMAN.value)]
        mock_translate_func.assert_has_calls(expected_calls, any_order=True)
        assert test_schema.summary == mock_translator.text
        assert test_schema.included_in_cover == mock_translator.text
        assert test_schema.excluded_from_cover == mock_translator.text
        assert test_schema.emergency_information == mock_translator.text

    def test_text_is_translated(self, mocker):
        test_text = "test text"
        mock_translated_response = "test_return_value"
        mock_translator = Mock()
        mock_translator.text = mock_translated_response
        mock_translate_func = mocker.patch('googletrans.Translator.translate', return_value=mock_translator)
        translation_service = TranslationServiceImpl()
        result = translation_service.translate_text(text=test_text, language=Language.GERMAN)
        mock_translate_func.assert_called_with(test_text, dest=Language.GERMAN.value)
        assert result == mock_translated_response

    def test_language_is_detected(self, mocker):
        test_text = "test text"
        mock_detected_language = "de"
        mock_translator = Mock()
        mock_translator.lang = mock_detected_language
        mock_translate_func = mocker.patch('googletrans.Translator.detect', return_value=mock_translator)
        translation_service = TranslationServiceImpl()
        detected_language = translation_service.detect_language(text=test_text)
        mock_translate_func.assert_called_with(test_text)
        assert detected_language == mock_detected_language