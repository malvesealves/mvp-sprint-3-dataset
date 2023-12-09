from pydantic import BaseModel
from typing import Optional, List
from model.candidato import Candidato
import json
import numpy as np

class CandidatoSchema(BaseModel):
    """ Define como um novo candidato a ser inserido deve ser representado
    """
    name: str = "Jon Doe"
    greScore: int = 323
    toeflScore: int = 111
    universityRating: int = 4
    statementPurpose: float = 3.6
    letterRecomendation: float = 2.6
    undergraduateGPA: float = 8.65
    researchExperience: int = 1


class CandidatoViewSchema(BaseModel):
    """ Define como um candidato será retornado
    """
    name: str = "Jon Doe"
    greScore: int = 323
    toeflScore: int = 111
    universityRating: int = 4
    statementPurpose: float = 3.6
    letterRecomendation: float = 2.6
    undergraduateGPA: float = 8.65
    researchExperience: int = 1
    chanceOfAdmit: int = None


class CandidatoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do candidato.
    """
    name: str = "Jon Doe"


class ListaCandidatosSchema(BaseModel):
    """ Define como uma listagem de canddatos será retornada.
    """
    candidatos:List[CandidatoSchema]


class CandidatoDelSchema(BaseModel):
    """ Define como um candidato para deleção será representado
    """
    name: str = "Jon Doe"


def apresenta_candidato(candidato: Candidato):
    """ Retorna uma representação do candidato seguindo o schema definido em
        CandidatoViewSchema.
    """
    return {
        "name": candidato.name,
        "greScore": candidato.greScore,
        "toeflScore": candidato.toeflScore,
        "universityRating": candidato.universityRating,
        "statementPurpose": candidato.statementPurpose,
        "letterRecomendation": candidato.letterRecomendation,
        "undergraduateGPA": candidato.undergraduateGPA,
        "researchExperience": candidato.researchExperience,
        "chanceOfAdmit": candidato.chanceOfAdmit
    }


def apresenta_candidatos(candidatos: List[Candidato]):
    """ Retorna uma representação do candidato seguindo o schema definido em
        CandidatoViewSchema.
    """
    result = []
    for candidato in candidatos:
        result.append({
            "name": candidato.name,
            "greScore": candidato.greScore,
            "toeflScore": candidato.toeflScore,
            "universityRating": candidato.universityRating,
            "statementPurpose": candidato.statementPurpose,
            "letterRecomendation": candidato.letterRecomendation,
            "undergraduateGPA": candidato.undergraduateGPA,
            "researchExperience": candidato.researchExperience,
            "chanceOfAdmit": candidato.chanceOfAdmit
        })

    return {"candidatos": result}

