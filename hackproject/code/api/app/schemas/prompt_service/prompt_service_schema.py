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
    language: str
    file_path: str

class WebText(BaseModel):
    body: str
    language: str

class WebPrompt(BaseModel):
    type: Union[WebDocument | WebText]
    chat_id: str

## processed prompt
class ProcessedDocument(BaseModel):
    document: List[LIDocument]
    doc_type: Document

class ProcessedPrompt(BaseModel):
    chat_id: str
    text: str = None
    language: Language
    document: ProcessedDocument = None
    product: Product