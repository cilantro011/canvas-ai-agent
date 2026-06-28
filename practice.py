assignments = [
    {"name": "Math Homework", "due_date": "2026-06-05"},
    {"name": "History Essay", "due_date": "2026-06-27"},
    {"name": "Physics Lab", "due_date": "2026-06-08"},
    {"name": "English Paper", "due_date": "2026-06-28"},
    {"name": "CS Project", "due_date": "2026-06-09"}
]

def get_assignment_names(assignments):
    names = []
    for assignment in assignments:
        names.append(assignment['name'])
    
    return names

print(get_assignment_names(assignments))
        