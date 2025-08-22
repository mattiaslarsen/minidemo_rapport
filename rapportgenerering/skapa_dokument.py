from docxtpl import DocxTemplate
from models.rapport import Rapport

def skapa_dokument(rapport: Rapport):
    """Skapar Word-dokument från rapportdata med Jinja2-mall"""
    doc = DocxTemplate("rapportgenerering/mall/wordmall.docx")
    # model_dump med json-mode konverterar enum till sträng automatiskt
    context = rapport.model_dump(mode='json')
    doc.render(context)
    doc.save("rapport_output.docx")
    print("✅ Word-dokument skapat: rapport_output.docx")
