from pypdf import PdfReader

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def read_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def create_pdf(text):

    file_name = "translated_document.pdf"

    pdfmetrics.registerFont(
        TTFont(
            "TamilFont",
            "fonts/NotoSansTamil-Regular.ttf"
        )
    )

    pdf = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    style = styles["BodyText"]

    style.fontName = "TamilFont"

    content = [
        Paragraph(text.replace("\n", "<br/>"), style)
    ]

    pdf.build(content)

    return file_name