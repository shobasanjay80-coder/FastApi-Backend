import google.generativeai as genai
from app.config.settings import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_interview_feedback(
        transcript,
        confidence_score,
        fluency_score,
        body_language_score
):

    prompt = f"""
    Analyze this mock interview performance.

    Transcript:
    {transcript}

    Scores:
    Confidence Score: {confidence_score}
    Fluency Score: {fluency_score}
    Body Language Score: {body_language_score}

    Provide:

    1. Overall performance summary
    2. Strengths
    3. Weaknesses
    4. Suggestions to improve interview performance
    """

    response = model.generate_content(prompt)

    return response.text