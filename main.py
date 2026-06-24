import datetime
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

result = get_upcoming_assignments(assignments)
print(result)
