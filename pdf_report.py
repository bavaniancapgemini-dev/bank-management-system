import reportlab.pdfgen # type: ignore

def create_pdf_report():

    pdf = reportlab.pdfgen.Canvas(
        "bank_report.pdf"
    )

    pdf.drawString(
        100,
        750,
        "Bank Management Report"
    )

    pdf.save()