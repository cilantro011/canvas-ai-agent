import datetime
import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("CANVAS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

def get_courses():  
    response = requests.get("https://uta.instructure.com/api/v1/courses", headers=headers)    
    data = response.json()
    return data

def get_course_names():
    response = requests.get("https://uta.instructure.com/api/v1/courses", headers=headers)    
    data = response.json()
    courses = []
    for a in data:
        try:
            courses.append({"name": a["name"], "id": a["id"]})
        except KeyError:
            continue
    return courses

def get_assignment(course_id):
    response = requests.get(f"https://uta.instructure.com/api/v1/courses/{course_id}/assignments", headers= headers)
    assignment = response.json()
    return assignment





    
