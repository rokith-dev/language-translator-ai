from pypdf import PdfReader
from fpdf import FPDF


def read_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def create_pdf(text):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    lines = text.split("\n")

    for line in lines:
        pdf.multi_cell(0, 10, line)

    file_name = "translated_document.pdf"

    pdf.output(file_name)

    return file_name