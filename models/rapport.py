from pydantic import BaseModel

class Rapport(BaseModel):
    sammanfattning: str
    aktivitet: str
    timmar: float
    kommentar: str
