from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

MOCK_AI = False

def generate_study_tips(assignment_name):
    if MOCK_AI:
        return "1. Review notes. 2. Practice problems. 3. Ask for help."
    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents = f"Give me 3 study tips in 3 sentences for this assignment: {assignment_name}"

    )
    return response.text
