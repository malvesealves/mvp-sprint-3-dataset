from pydantic import BaseModel
from typing import Optional, List
from model.vinho import Vinho
import json
import numpy as np

class VinhoSchema(BaseModel):
    """ Define como um novo vinho a ser inserido deve ser representado
    """
    name: str = "Jon Doe"
    greScore: int = 323
    toeflScore: int = 111
    universityRating: int = 4
    statementPurpose: float = 3.6
    letterRecomendation: float = 2.6
    undergraduateGPA: float = 8.65
    researchExperience: int = 1


class VinhoViewSchema(BaseModel):
    """ Define como um vinho será retornado
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


class VinhoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do vinho.
    """
    name: str = "Jon Doe"


class ListaVinhosSchema(BaseModel):
    """ Define como uma listagem de vinhos será retornada.
    """
    vinhos:List[VinhoSchema]


class VinhoDelSchema(BaseModel):
    """ Define como um vinho para deleção será representado
    """
    name: str = "Jon Doe"


def apresenta_vinho(vinho: Vinho):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    return {
        "name": vinho.name,
        "greScore": vinho.greScore,
        "toeflScore": vinho.toeflScore,
        "universityRating": vinho.universityRating,
        "statementPurpose": vinho.statementPurpose,
        "letterRecomendation": vinho.letterRecomendation,
        "undergraduateGPA": vinho.undergraduateGPA,
        "researchExperience": vinho.researchExperience,
        "chanceOfAdmit": vinho.chanceOfAdmit
    }


def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
            "name": vinho.name,
            "greScore": vinho.greScore,
            "toeflScore": vinho.toeflScore,
            "universityRating": vinho.universityRating,
            "statementPurpose": vinho.statementPurpose,
            "letterRecomendation": vinho.letterRecomendation,
            "undergraduateGPA": vinho.undergraduateGPA,
            "researchExperience": vinho.researchExperience,
            "chanceOfAdmit": vinho.chanceOfAdmit
        })

    return {"vinhos": result}

