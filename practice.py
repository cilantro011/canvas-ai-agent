import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("CANVAS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}



assignments = [
    {"name": "Math Homework", "due_date": "2026-06-05"},
    {"name": "History Essay", "due_date": "2026-06-27"},
    {"name": "Physics Lab", "due_date": "2026-06-08"},
    {"name": "English Paper", "due_date": "2026-06-28"},
    {"name": "CS Project", "due_date": "2026-06-09"}
]

def get_courses():
    response = requests.get("https://uta.instructure.com/api/v1/courses", headers=headers)
    data = response.json()
    courses = []
   
    for course in data:
        try:
            courses.append(course['name'])
        except KeyError:
            continue
    return courses
def get_assignment_names(assignments):
    names = []
    for assignment in assignments:
        names.append(assignment['name'])
    
    return names


print(get_courses())
        