import requests
import os
import json
from dotenv import load_dotenv
import datetime

load_dotenv()

canvas_token = os.getenv("CANVAS_TOKEN")
headers = {"Authorization": f"Bearer {canvas_token}"}

def get_course_name():
    response = requests.get("https://uta.instructure.com/api/v1/courses", headers = headers)
    data = response.json()
    courses = []
    for a in data:
        try:
            courses.append({'name': a['name'], 'id': a['id']})
        except KeyError:
            continue
    return courses

courses = get_course_name()

def get_assignments_name(course_id):   
    response = requests.get(f"https://uta.instructure.com/api/v1/courses/{course_id}/assignments", headers = headers)
    data = response.json()
    assignment_names= []
    for assignment in data:
        try:
            assignment_names.append(assignment['name'])
        except KeyError:
            continue
    return assignment_names

assignments = []
for course in courses:
    assignments.append(course['name'])
    assignments.append(get_assignments_name(course['id']))
    
print(assignments)
    
    