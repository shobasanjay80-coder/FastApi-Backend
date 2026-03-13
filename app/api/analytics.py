from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Interview, Resume, Assignment
from app.core.auth_dependency import get_current_user

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/dashboard")
def dashboard(user=Depends(get_current_user), db: Session = Depends(get_db)):

    interviews = db.query(Interview).filter(Interview.user_id == user.id).all()
    resumes = db.query(Resume).filter(Resume.user_id == user.id).all()
    assignments = db.query(Assignment).filter(Assignment.user_id == user.id).all()

    avg_confidence = (
        sum(i.confidence_score for i in interviews) / len(interviews)
        if interviews else 0
    )

    avg_fluency = (
        sum(i.fluency_score for i in interviews) / len(interviews)
        if interviews else 0
    )

    return {
        "interviews_completed": len(interviews),
        "resume_uploaded": len(resumes),
        "assignments_done": len(assignments),
        "average_confidence": avg_confidence,
        "average_fluency": avg_fluency
    }