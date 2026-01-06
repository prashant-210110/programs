from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(text, filename="weather_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    text_object = c.beginText(40, height - 50)
    text_object.setFont("Helvetica", 12)

    for line in text.split(". "):
        text_object.textLine(line)

    c.drawText(text_object)
    c.save()

    return filename
