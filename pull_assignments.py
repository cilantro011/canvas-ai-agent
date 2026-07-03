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
            #assignment_names.append(assignment['name'])
            assignment_names.append ({
                'name': assignment['name'],
                'due_at': assignment['due_at']
            })
        except KeyError:
            continue
    return assignment_names

def get_upcoming_assignments(assignments):
    start = datetime.date(2026, 4, 1)
    end = datetime.date(2026, 4, 10)
    upcoming_assignments = []
    for course in assignments:
        due_assignments = []
        for assignment in course['assignments']:
            try:
                due_at = datetime.datetime.strptime(assignment["due_at"], "%Y-%m-%dT%H:%M:%SZ").date()
            except (ValueError, TypeError):
                continue
            if due_at >= start and due_at <= end:
                due_assignments.append({
                    'name': assignment['name'],
                    'due_at': assignment['due_at']
                })
        upcoming_assignments.append({'course': course['course'], 'assignments': due_assignments})
    
    return upcoming_assignments

assignments = []             
for course in courses:
    assignments.append({'course':course['name'],
                        'assignments': get_assignments_name(course['id'])})
    
    
print(assignments)

print(get_upcoming_assignments(assignments))
    