from pydantic import BaseModel, validator
from typing import Optional
from hackproject.code.api.app.enums import TTSModel

class TTS(BaseModel):
    text: str
    language: Optional[str] = 'en'

    @validator('language')
    def validate_language(cls, v):
        if v.upper() not in TTSModel.__members__.keys():
            raise ValueError('language option is not valid')
        return v
