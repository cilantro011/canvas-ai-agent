
from pdf_generator import create_pdf
from ai_generator import generate_study_tips
from pull_assignments import get_all_assignments, get_upcoming_assignments

def run_pipeline():
    assignments = get_all_assignments()
    upcoming_assignments = get_upcoming_assignments(assignments)
    for course in upcoming_assignments:
        for assignment in course['assignments']:
            #print(f"{course['course']}: {assignment['name']}: {generate_study_tips(assignment['name'])}")
            print(assignment['description'])
    #create_pdf("study_guide.pdf", upcoming_assignments)

run_pipeline()    
if __name__ == '__main__':
    run_pipeline()
    
