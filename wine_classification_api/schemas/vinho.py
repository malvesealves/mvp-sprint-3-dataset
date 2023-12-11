from pydantic import BaseModel
from typing import Optional, List
from model.vinho import Vinho
import json
import numpy as np

class VinhoSchema(BaseModel):
    """ Define como um novo vinho a ser inserido deve ser representado
    """
    name: str = "Amostra_1"
    fixedAcidity: float = 323.1
    volatileAcidity: float = 111.1
    citricAcid: float = 1.1
    residualSugar: float = 3.6
    chlorides: float = 2.6
    freeSulfurDioxide: float = 8.65
    totalSulfurDioxide: float = 1.1
    density: float = 1.1
    ph: float = 1.1
    sulphates: float = 1.1
    alcohol: float = 1.1

class VinhoViewSchema(BaseModel):
    """ Define como um vinho será retornado
    """
    name: str = "Amostra_1"
    fixedAcidity: float = 323.1
    volatileAcidity: float = 111.1
    citricAcid: float = 1.1
    residualSugar: float = 3.6
    chlorides: float = 2.6
    freeSulfurDioxide: float = 8.65
    totalSulfurDioxide: float = 1.1
    density: float = 1.1
    ph: float = 1.1
    sulphates: float = 1.1
    alcohol: float = 1.1
    quality: int = None

class VinhoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do vinho.
    """
    name: str = "Amostra_1"


class ListaVinhosSchema(BaseModel):
    """ Define como uma listagem de vinhos será retornada.
    """
    vinhos:List[VinhoSchema]


class VinhoDelSchema(BaseModel):
    """ Define como um vinho para deleção será representado
    """
    name: str = "Amostra_1"


def apresenta_vinho(vinho: Vinho):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    return {
        "name": vinho.name,
        "fixedAcidity": vinho.fixedAcidity,
        "volatileAcidity": vinho.volatileAcidity,
        "citricAcid": vinho.citricAcid,
        "residualSugar": vinho.residualSugar,
        "chlorides": vinho.chlorides,
        "freeSulfurDioxide": vinho.freeSulfurDioxide,
        "totalSulfurDioxide": vinho.totalSulfurDioxide,
        "density": vinho.density,
        "ph": vinho.ph,
        "sulphates": vinho.sulphates,
        "alcohol": vinho.alcohol,
        "quality": vinho.quality
    }


def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
            "name": vinho.name,
            "fixedAcidity": vinho.fixedAcidity,
            "volatileAcidity": vinho.volatileAcidity,
            "citricAcid": vinho.citricAcid,
            "residualSugar": vinho.residualSugar,
            "chlorides": vinho.chlorides,
            "freeSulfurDioxide": vinho.freeSulfurDioxide,
            "totalSulfurDioxide": vinho.totalSulfurDioxide,
            "density": vinho.density,
            "ph": vinho.ph,
            "sulphates": vinho.sulphates,
            "alcohol": vinho.alcohol,
            "quality": vinho.quality
        })

    return {"vinhos": result}

