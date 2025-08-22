from pydantic import BaseModel
from enum import Enum

class AnsvarigPerson(Enum):
    MARCUS = "Marcus"
    LAMBROS = "Lambros"
    SLAVKO = "Slavko"

class Rapport(BaseModel):
    sammanfattning: str
    aktivitet: str
    timmar: float
    kommentar: str
    ansvarig: AnsvarigPerson
