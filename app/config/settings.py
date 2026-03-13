import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
load_dotenv()

# Base directory of project
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings:
    """
    Global application configuration
    """

    # App
    APP_NAME: str = os.getenv("APP_NAME", "AI Interview Platform")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/interview_ai"
    )

    # AI API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    # Upload directories
    VIDEO_UPLOAD_DIR: str = os.getenv(
        "UPLOAD_VIDEO_DIR",
        str(BASE_DIR / "uploads/videos")
    )

    AUDIO_UPLOAD_DIR: str = os.getenv(
        "UPLOAD_AUDIO_DIR",
        str(BASE_DIR / "uploads/audio")
    )

    RESUME_UPLOAD_DIR: str = os.getenv(
        "UPLOAD_RESUME_DIR",
        str(BASE_DIR / "uploads/resumes")
    )

    # Video analysis settings
    MAX_VIDEO_SIZE_MB: int = 100

    # Speech analysis
    MAX_AUDIO_LENGTH_MINUTES: int = 10

    # Interview settings
    MAX_INTERVIEW_QUESTIONS: int = 5

    # Resume scoring
    MAX_RESUME_SCORE: int = 100


# create settings instance
settings = Settings()


def create_upload_dirs():
    """
    Ensure upload directories exist
    """

    os.makedirs(settings.VIDEO_UPLOAD_DIR, exist_ok=True)
    os.makedirs(settings.AUDIO_UPLOAD_DIR, exist_ok=True)
    os.makedirs(settings.RESUME_UPLOAD_DIR, exist_ok=True)