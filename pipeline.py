from main import get_assignment, get_course_names
from pdf_generator import create_pdf
from ai_generator import generate_study_tips
from pull_assignments import get_all_assignments, get_upcoming_assignments

def run_pipeline():
    assignments = get_all_assignments()
    upcoming_assignments = get_upcoming_assignments(assignments)
    for course in upcoming_assignments:
        for assignment in course['assignments']:
            print(f"{assignment['name']}: {generate_study_tips(assignment['name'])}")

run_pipeline()
    
