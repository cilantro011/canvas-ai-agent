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

def get_assignments(course_id):
    response = requests.get(f"https://uta.instructure.com/api/v1/courses/{course_id}/assignments", headers = headers)
    data = response.json()
    return data

def get_assignment_names(assignments):
    names = []
    for assignment in assignments:
        names.append(assignment['name'])
    
    return names

def safe_get(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return "N/A"

test_assignment = get_assignments(265649)
with open("test.json", "w") as f:
    json.dump(test_assignment, f, indent = 4)
print(safe_get( {"name": "Math Homework", "due_date": "2026-06-05"}, 'name'))
print(get_courses())
        