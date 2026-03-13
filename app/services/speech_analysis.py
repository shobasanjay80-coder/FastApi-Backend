import re
import google.generativeai as genai
from app.config.settings import settings


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "actually",
    "basically",
    "so",
    "okay"
]


def transcribe_audio(audio_path: str):

    with open(audio_path, "rb") as audio_file:

        response = model.generate_content(
            [
                "Transcribe this interview audio accurately.",
                {"mime_type": "audio/wav", "data": audio_file.read()}
            ]
        )

    transcript = response.text

    return transcript


def count_filler_words(text: str):

    text = text.lower()

    filler_count = 0

    for word in FILLER_WORDS:

        filler_count += len(re.findall(rf"\b{word}\b", text))

    return filler_count


def speech_metrics(transcript: str, duration_seconds: float):

    words = transcript.split()

    total_words = len(words)

    minutes = duration_seconds / 60 if duration_seconds else 1

    words_per_minute = total_words / minutes

    filler_count = count_filler_words(transcript)

    fluency_score = max(0, 100 - (filler_count * 3))

    return {
        "words_per_minute": words_per_minute,
        "filler_words": filler_count,
        "fluency_score": fluency_score
    }