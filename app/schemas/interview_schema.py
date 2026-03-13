from pydantic import BaseModel
from datetime import datetime


# -------------------------
# INTERVIEW CREATE
# -------------------------
class InterviewCreate(BaseModel):

    role: str


# -------------------------
# INTERVIEW RESULT
# -------------------------
class InterviewResult(BaseModel):

    confidence_score: float
    fluency_score: float
    body_language_score: float
    feedback: str


# -------------------------
# INTERVIEW RESPONSE
# -------------------------
class InterviewResponse(BaseModel):

    id: int
    role: str
    video_path: str
    transcript: str
    confidence_score: float
    fluency_score: float
    body_language_score: float
    feedback: str
    created_at: datetime

    class Config:
        orm_mode = True