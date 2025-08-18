from docxtpl import DocxTemplate
from models.rapport import Rapport

def skapa_dokument(rapport: Rapport):
    """Skapar Word-dokument från rapportdata med Jinja2-mall"""
    doc = DocxTemplate("rapportgenerering/mall/wordmall.docx")
    context = rapport.dict()
    doc.render(context)
    doc.save("rapport_output.docx")
    print("✅ Word-dokument skapat: rapport_output.docx")
