from main import get_assignment, get_course_names, get_upcoming_assignments
from pdf_generator import create_pdf
from ai_generator import generate_study_tips

def run_pipeline():
    course_name = get_course_names()
    create_pdf("result.pdf", course_name)

run_pipeline()
    
