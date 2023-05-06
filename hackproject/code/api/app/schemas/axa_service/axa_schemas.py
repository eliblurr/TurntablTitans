from pydantic import BaseModel, validator
from typing import List, Optional

class Answer(BaseModel):
    id: str
    answer: Optional[str]
    priority: Optional[int]

class Question(BaseModel):
    id: str
    order: int
    question: str

class QuestionDetail(BaseModel):
    id: str
    order: int
    question: str
    possible_answers: List[Answer]

class State(BaseModel):
    id:str # question_id
    value: str #answer
    order: int

class Line(BaseModel):
    lines: List[State] = []
    line_ref: str = "string"

class Claim(BaseModel):
    lines: List[Line] = []

class Coverage(BaseModel):
    priority: int
    status: str

class SubmissionResponse(BaseModel):
    coverage: Optional[List[Coverage]] = []
    next_question: Optional[Question]
    progress: Optional[int]
    states: List[State] = []

class Product(BaseModel):
    id:str
    name: str