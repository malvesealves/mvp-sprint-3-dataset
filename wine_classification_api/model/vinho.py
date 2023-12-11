from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = FixedAcidity,VolatileAcidity,CitricAcid,ResidualSugar,Chlorides,
#           FreeSulfurDioxide,TotalSulfurDioxide,Density,Ph,Sulphates,Alcohol,Quality

class Vinho(Base):
    __tablename__ = 'vinhos'
    
    name = Column("Name", String(50),primary_key=True)
    fixed_acidity= Column("FixedAcidity", Float)
    volatile_acidity = Column("VolatileAcidity", Float)
    citric_acid = Column("CitricAcid", Float)
    residual_sugar = Column("ResidualSugar", Float)
    chlorides = Column("Chlorides", Float)
    free_sulfur_dioxide = Column("FreeSulfurDioxide", Float)
    total_sulfur_dioxide = Column("TotalSulfurDioxide", Float)
    density = Column("Density", Float)
    ph = Column("Ph", Float)
    sulphates = Column("Sulphates", Float)
    alcohol = Column("Alcohol", Float)    
    quality = Column("Quality", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str, fixed_acidity:float, volatile_acidity:float, citric_acid:float, residual_sugar:float,
                 chlorides:float, free_sulfur_dioxide:float, total_sulfur_dioxide:float, density:float,
                 ph:float, sulphates:float, alcohol:float, quality:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Vinho

        Arguments:   
            name: nome da amostra de vinho 
            fixedAcidity: composto pela maioria dos ácidos envolvidos com vinho, fixos ou não voláteis (não evaporam facilmente)
            volatileAcidity: quantidade de ácido acético no vinho, na qual a níveis muito altos pode levar a um gosto desagradável
            citricAcid: encontrado em pequenas quantidades, ácido cítrico pode adicionar refrescância e sabor aos vinhos
            residualSugar: quantidade de açúcar remanascente depois dos descansos de fermentação
            chlorides: quantidade de sais no vinho
            freeSulfurDioxide: forma livre de SO2 existente entre SO2 molecular (como gás dissolvido) e íon bissulfito
            totalSulfurDioxide: quantidade de SO2 livre e vinculado
            density: a densidade do vinho é próxima da densidade da água dependendo do percentual de álcool e açúcar contido
            ph: descreve quão ácido ou básico o vinho é numa escala de o (muito ácido) até 14 (muito básico)
            sulphates: um aditivo do vinho que pode contribuir os níveis de gás dióxido de enxofre
            alcohol: percentual de álcool contido no vinho
            quality: qualidade do vinho, avaliada com notas entre 0 e 10 (originalmente) e notas 0 ou 1 (pós tratamento)
            data_insercao: data de quando o vinho foi inserido à base
        """
        self.name = name
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.ph = ph
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao