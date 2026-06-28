from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def generate_study_tips(assignment_name):
    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents = f"Give me 3 study tips for this assignment: {assignment_name}"

    )
    return response.text

print(generate_study_tips("Building with gemini quiz"))