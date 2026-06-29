from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap
from ai_generator import generate_study_tips

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
        
        c.drawString(x, y, f"{assignment['name']}")
        y -= 15
        wrapped = textwrap.wrap(generate_study_tips(assignment['name']), width = 80)
        for line in wrapped:
            c.drawString(x,y, line)
            y -= 15
    c.save()