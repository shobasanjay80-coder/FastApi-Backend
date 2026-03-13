from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Resume
from app.core.auth_dependency import get_current_user
from app.utils.file_handler import save_upload_file
from app.utils.pdf_parser import extract_text_from_pdf, clean_resume_text
from app.services.resume_analysis import analyze_resume
from app.config.settings import settings

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),   # IMPORTANT
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    file_path = await save_upload_file(file, settings.RESUME_UPLOAD_DIR)

    text = extract_text_from_pdf(file_path)

    cleaned_text = clean_resume_text(text)

    analysis = analyze_resume(cleaned_text)

    resume = Resume(
        user_id=user.id,
        file_path=file_path,
        extracted_text=cleaned_text,
        score=80,
        feedback=analysis["feedback"]
    )

    db.add(resume)
    db.commit()

    return analysis