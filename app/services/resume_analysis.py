import google.generativeai as genai
from app.config.settings import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def analyze_resume(resume_text: str):

    prompt = f"""
    Analyze this resume.

    Give:
    1. Resume score out of 100
    2. Strengths
    3. Weaknesses
    4. Suggestions to improve

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return {
        "feedback": response.text
    }