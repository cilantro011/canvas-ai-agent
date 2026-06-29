import datetime
import json
import requests
from dotenv import load_dotenv
import os

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

def get_total_points(assignments):
    total_points = 0
    for assignment in assignments:
        total_points += assignment["points"]
    return total_points

def get_overdue_assignments(assignments):
    overdue_assignments = []
    for assignment in assignments:
        try:
            due_date = datetime.datetime.strptime(assignment["due_date"], "%Y-%m-%d").date()
        except ValueError:
            continue
        if due_date < datetime.date.today():  
            overdue_assignments.append(assignment)
    return overdue_assignments

def get_upcoming_assignments(assignments):
    upcoming_assignments = []
    for assignment in assignments:
        try:
            due_date = datetime.datetime.strptime(assignment["due_date"], "%Y-%m-%d").date()
        except ValueError:
            continue
            
        if due_date > datetime.date.today() and due_date <= datetime.date.today() + datetime.timedelta(days=7):
            upcoming_assignments.append(assignment)
            
    return upcoming_assignments

def save_results(assignments):
    with open("save_results.txt", "w") as f:
        for assignment in assignments:
                f.write(f"{assignment['name']}\n")

def read_results():
    with open("save_results.txt", "r") as f:
        a = f.readlines()
        for line in a:
            print(line)
            
def save_to_json(assignments):
    with open("assignments.json", "w") as f:
        json.dump(assignments, f)
        
def load_from_json():
    with open("assignments.json", "r") as f:
        return json.load(f)
        
        
def get_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    print(response.status_code)
    
    if response.status_code == 200:
      return{
                "login":data['login'], 
                "public_repos": data['public_repos'],
                "followers": data['followers']}
    else:
        return "User not found"
    
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
    
if __name__ == "__main__":
    save_to_json(assignments)
    print(load_from_json())
    print(f"Upcoming assignments :  {get_upcoming_assignments(assignments)}")
    save_results(assignments)
    read_results()

    #username = input("Enter your github username: ")
    #print(get_github_user(username)) 
    courses = get_courses()
    with open("courses.json", 'w') as f:
        json.dump(courses, f, indent = 4)

    #print(get_course_names())

    print(get_assignment(256118))




    
