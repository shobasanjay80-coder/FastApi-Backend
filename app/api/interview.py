from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.models import Interview
from app.core.auth_dependency import get_current_user
from app.utils.file_handler import save_upload_file
from app.utils.video_processor import extract_audio_from_video, get_video_duration
from app.config.settings import settings

from app.services.speech_analysis import transcribe_audio, speech_metrics
from app.services.video_analysis import analyze_video
from app.services.ai_service import generate_interview_feedback

router = APIRouter(prefix="/interview", tags=["Interview"])


@router.post("/upload")
async def upload_interview(
        role: str,
        video: UploadFile = File(...),
        user=Depends(get_current_user),
        db: Session = Depends(get_db)
):

    video_path = await save_upload_file(video, settings.VIDEO_UPLOAD_DIR)

    audio_path = extract_audio_from_video(video_path)

    transcript = transcribe_audio(audio_path)

    duration = get_video_duration(video_path)

    speech_data = speech_metrics(transcript, duration)

    video_data = analyze_video(video_path)

    feedback = generate_interview_feedback(
        transcript,
        video_data["confidence_score"],
        speech_data["fluency_score"],
        video_data["body_language_score"]
    )

    interview = Interview(
        user_id=user.id,
        role=role,
        video_path=video_path,
        transcript=transcript,
        confidence_score=video_data["confidence_score"],
        fluency_score=speech_data["fluency_score"],
        body_language_score=video_data["body_language_score"],
        feedback=feedback
    )

    db.add(interview)
    db.commit()

    return {
        "confidence_score": video_data["confidence_score"],
        "fluency_score": speech_data["fluency_score"],
        "feedback": feedback
    }