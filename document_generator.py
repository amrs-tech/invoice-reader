from docx import Document

def create_doc(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)
