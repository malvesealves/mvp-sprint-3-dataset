from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Candidato(Base):
    __tablename__ = 'candidatos'

    name = Column("Name", String(50),primary_key=True)
    greScore = Column("GREScore", Integer)
    toeflScore = Column("TOEFLScore", Integer)
    universityRating = Column("UniversityRating", Integer)
    statementPurpose = Column("StatementPurpose", Float)
    letterRecomendation = Column("LetterRecomendation", Float)
    undergraduateGPA = Column("undergraduateGPA", Float)
    researchExperience = Column("ResearchExperience", Integer)
    chanceOfAdmit = Column("chanceOfAdmit", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())



    def __init__(self, name:str, greScore:int, toeflScore:int,
                 universityRating:int, statementPurpose:float, letterRecomendation:float,
                 undergraduateGPA:float, researchExperience:int,
                 chanceOfAdmit:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Candidato

        Arguments:
            Name: nome do candidato.
            GRE Score: nota GRE do candidato
            TOEFL Score: nota TOEFL do candidato
            University Rating: avaliação da universidade pretendida do candidato
            Statement Of Purpose: justificativa de aplicação do candidato
            Letter Of Recomendation: avaliação da carta de recomendação do candidato
            Undergraduate GPA: nota GPA do ensino médio do candidato
            Research Experience: nota de experiência de pesquisa do usuário
            Chance Of Admit: chance de admissão 0 Não e 1 Sim
            data_insercao: data de quando o candidato foi inserido à base
        """

        self.name = name
        self.greScore = greScore
        self.toeflScore = toeflScore
        self.universityRating = universityRating
        self.statementPurpose = statementPurpose
        self.letterRecomendation = letterRecomendation
        self.undergraduateGPA = undergraduateGPA
        self.researchExperience = researchExperience
        self.chanceOfAdmit = chanceOfAdmit

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
