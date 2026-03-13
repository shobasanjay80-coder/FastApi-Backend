from pydantic import BaseModel
from datetime import datetime


# -------------------------
# ASSIGNMENT GENERATE
# -------------------------
class AssignmentGenerate(BaseModel):

    role: str
    difficulty: str


# -------------------------
# ASSIGNMENT SUBMIT
# -------------------------
class AssignmentSubmit(BaseModel):

    question: str
    answer: str


# -------------------------
# ASSIGNMENT RESPONSE
# -------------------------
class AssignmentResponse(BaseModel):

    id: int
    question: str
    answer: str
    score: float
    feedback: str
    created_at: datetime

    class Config:
        orm_mode = True