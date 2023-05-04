from llama_index.indices.base import BaseGPTIndex
from pydantic import BaseModel

from hackproject.code.api.app.enums import Language


class IndexInformation(BaseModel):
    index: BaseGPTIndex
    language: Language

    class Config:
        arbitrary_types_allowed = True