from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
assignments = [
    {"name": "Math Homework", "due_date": "2026-06-05"},
    {"name": "History Essay", "due_date": "2026-06-27"},
    {"name": "Physics Lab", "due_date": "2026-06-08"},
    {"name": "English Paper", "due_date": "2026-06-28"},
    {"name": "CS Project", "due_date": "2026-06-09"}
]

def create_pdf(filename, assignments):
    c = canvas.Canvas(filename, pagesize=A4)
    x = 75
    y = 800
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y, "Upcoming Assignments")
    c.line(75, 790, 270, 790)
    y = 750
    c.setFont("Helvetica", 12)
    for assignment in assignments:
        
        c.drawString(x, y, f"{assignment['name']} - Due_date: {assignment['due_date']}")
        y -= 15
    c.save()

create_pdf("test.pdf", assignments)