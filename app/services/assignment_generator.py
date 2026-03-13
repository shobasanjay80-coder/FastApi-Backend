import google.generativeai as genai
from app.config.settings import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def generate_assignment(role, difficulty):

    prompt = f"""
    Generate a coding assignment.

    Role: {role}
    Difficulty: {difficulty}

    Include:
    - Problem statement
    - Requirements
    - Expected output
    """

    response = model.generate_content(prompt)

    return response.text