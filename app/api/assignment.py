from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Assignment
from app.core.auth_dependency import get_current_user
from app.schemas.assignment_schema import AssignmentGenerate, AssignmentSubmit
from app.services.assignment_generator import generate_assignment

import google.generativeai as genai
from app.config.settings import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

router = APIRouter(prefix="/assignment", tags=["Assignment"])


@router.post("/generate")
def create_assignment(data: AssignmentGenerate):

    assignment = generate_assignment(data.role, data.difficulty)

    return {"assignment": assignment}


@router.post("/submit")
def submit_assignment(
        data: AssignmentSubmit,
        user=Depends(get_current_user),
        db: Session = Depends(get_db)
):

    prompt = f"""
    Evaluate this assignment answer.

    Question:
    {data.question}

    Answer:
    {data.answer}

    Provide:
    - Score out of 100
    - Feedback
    """

    response = model.generate_content(prompt)

    feedback = response.text

    score = 80

    assignment = Assignment(
        user_id=user.id,
        question=data.question,
        answer=data.answer,
        score=score,
        feedback=feedback
    )

    db.add(assignment)
    db.commit()

    return {
        "score": score,
        "feedback": feedback
    }