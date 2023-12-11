from pydantic import BaseModel
from typing import Optional, List
from model.vinho import Vinho
import json
import numpy as np

class VinhoSchema(BaseModel):
    """ Define como um novo vinho a ser inserido deve ser representado
    """
    name: str = "Amostra1"
    fixedAcidity: float = 7.9
    volatileAcidity: float = 0.58
    citricAcid: float = 0.27
    residualSugar: float = 1.5
    chlorides: float = 0.116
    freeSulfurDioxide: float = 10.0
    totalSulfurDioxide: float = 28.0
    density: float = 0.9972
    ph: float = 3.24
    sulphates: float = 1.53
    alcohol: float = 9.2

class VinhoViewSchema(BaseModel):
    """ Define como um vinho será retornado
    """
    name: str = "Amostra1"
    fixedAcidity: float = 7.9
    volatileAcidity: float = 0.58
    citricAcid: float = 0.27
    residualSugar: float = 1.5
    chlorides: float = 0.116
    freeSulfurDioxide: float = 10.0
    totalSulfurDioxide: float = 28.0
    density: float = 0.9972
    ph: float = 3.24
    sulphates: float = 1.53
    alcohol: float = 9.2
    quality: int = None

class VinhoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do vinho.
    """
    name: str = "Amostra1"


class ListaVinhosSchema(BaseModel):
    """ Define como uma listagem de vinhos será retornada.
    """
    vinhos:List[VinhoSchema]


class VinhoDelSchema(BaseModel):
    """ Define como um vinho para deleção será representado
    """
    name: str = "Amostra1"


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

