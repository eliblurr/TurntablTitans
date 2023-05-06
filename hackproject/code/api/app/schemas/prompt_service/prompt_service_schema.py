from typing import List

from llama_index import Document as LIDocument
from pydantic import BaseModel
from pydantic.class_validators import Union

from hackproject.code.api.app.enums import Language, Document, Product


class ChatInitialization(BaseModel):
    product: Product
    chat_id: str = None

## web prompts
class WebDocument(BaseModel):
    type: Document
    doc_language: str
    file_path: str
    native_language: str

class WebText(BaseModel):
    body: str
    native_language: str

class WebPrompt(BaseModel):
    prompt: Union[WebDocument | WebText]
    chat_id: str

## processed prompt
class ProcessedDocument(BaseModel):
    document: List[LIDocument]
    doc_type: Document
    doc_language: Language

class ProcessedPrompt(BaseModel):
    chat_id: str
    text: str = None
    native_language: Language
    document: ProcessedDocument = None
    product: Product