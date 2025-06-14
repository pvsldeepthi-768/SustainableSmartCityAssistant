from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

class Message(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str
