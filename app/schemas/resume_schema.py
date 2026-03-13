from pydantic import BaseModel
from datetime import datetime


# -------------------------
# RESUME ANALYSIS RESPONSE
# -------------------------
class ResumeAnalysis(BaseModel):

    score: float
    feedback: str


# -------------------------
# RESUME RESPONSE
# -------------------------
class ResumeResponse(BaseModel):

    id: int
    file_path: str
    extracted_text: str
    score: float
    feedback: str
    created_at: datetime

    class Config:
        orm_mode = True