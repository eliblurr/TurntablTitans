from pydantic import BaseModel

class InsuranceDocumentResponseSchema(BaseModel):
    summary: str
    included_in_cover: str
    excluded_from_cover: str
    emergency_information: str