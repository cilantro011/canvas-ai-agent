import requests
import os
import json
from dotenv import load_dotenv
import datetime
from bs4 import BeautifulSoup

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



def get_assignments_name(course_id):   
    response = requests.get(f"https://uta.instructure.com/api/v1/courses/{course_id}/assignments", headers = headers)
    data = response.json()
    assignment_names= []
    for assignment in data:
        try:
            #assignment_names.append(assignment['name'])
            assignment_names.append ({
                'name': assignment['name'],
                'due_at': assignment['due_at'],
                'description': assignment['description']
            })
        except KeyError:
            continue
    return assignment_names

def get_all_assignments():
    courses = get_course_name()
    assignments = []             
    for course in courses:
        assignments.append({'course':course['name'],
                            'assignments': get_assignments_name(course['id'])})
    
    return assignments

def strip_html(html):
    if not html:
        return ""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def get_upcoming_assignments(assignments):
    start = datetime.date.today()
    end = datetime.date.today() + datetime.timedelta(days=30)
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
           
                    'due_at': assignment['due_at'],
                    'description': strip_html(assignment['description'])
                })
        if due_assignments:
            upcoming_assignments.append({'course': course['course'], 'assignments': due_assignments})
    
    return upcoming_assignments

