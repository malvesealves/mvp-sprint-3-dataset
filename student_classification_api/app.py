from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Candidato, Model
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="Graduate Admission API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
candidato_tag = Tag(name="Candidato", description="Adição, visualização e remoção de candidatos à base")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de candidatos
@app.get('/candidatos', tags=[candidato_tag],
         responses={"200": CandidatoViewSchema, "404": ErrorSchema})
def get_candidatos():
    """Faz a busca por todos os Candidatos cadastrados
        Retorna uma representação da listagem de Candidatos.
    """
    logger.debug(f"Coletando candidatos ")
    
    # criando conexão com a base
    session = Session()
    
    # fazendo a busca
    candidatos = session.query(Candidato).all()

    if not candidatos:
        logger.warning("Não há candidatos cadastrados na base :/")
        return {"message": "Não há candidatos cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d candidatos encontrados" % len(candidatos))
        return apresenta_candidatos(candidatos), 200


# Rota de adição de candidato
@app.post('/candidato', tags=[candidato_tag],
          responses={"200": CandidatoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: CandidatoSchema):
    """Adiciona um novo candidato à base de dados
    Retorna uma representação dos candidatos e predições associadas.
    """

    # Carregando modelo do Google colab incluso no Github
    ml_path = 'ml_model/Admission.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    candidato = Candidato(
        name=form.name.strip(), 
        greScore=form.greScore, 
        toeflScore=form.toeflScore, 
        universityRating=form.universityRating, 
        statementPurpose=form.statementPurpose, 
        letterRecomendation=form.letterRecomendation, 
        undergraduateGPA=form.undergraduateGPA, 
        researchExperience=form.researchExperience,
        chanceOfAdmit=Model.preditor(modelo, form)
    )

    logger.debug(f"Adicionando candidato de nome: '{candidato.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se candidato já existe na base
        if session.query(Candidato).filter(Candidato.name == form.name).first():
            error_msg = "Candidato já existente na base :/"
            logger.warning(f"Erro ao adicionar candidato '{candidato.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando candidato
        session.add(candidato)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado candidato de nome: '{candidato.name}'")
        return apresenta_candidato(candidato), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo candidato :/"
        logger.warning(f"Erro ao adicionar candidato '{candidato.name}', {error_msg}")
        return {"message": error_msg}, 400


# Rota de busca de candidato por nome
@app.get('/candidato', tags=[candidato_tag],
         responses={"200": CandidatoViewSchema, "404": ErrorSchema})
def get_candidato(query: CandidatoBuscaSchema):    
    """Faz a busca por um candidato cadastrado na base a partir do nome
    """
    
    candidato_nome = query.name
    logger.debug(f"Coletando dados sobre candidato #{candidato_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    candidato = session.query(Candidato).filter(Candidato.name == candidato_nome).first()
    
    if not candidato:
        # se o candidato não foi encontrado
        error_msg = f"Candidato {candidato_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar candidato '{candidato_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Candidato encontrado: '{candidato.name}'")
        # retorna a representação do candidato
        return apresenta_candidato(candidato), 200


# Rota de remoção de candidato por nome
@app.delete('/candidato', tags=[candidato_tag],
            responses={"200": CandidatoViewSchema, "404": ErrorSchema}) #responses={"200": CandidatoDelSchema, "404": ErrorSchema})
def delete_candidato(query: CandidatoBuscaSchema):
    """Deleta um Candidato a partir do nome informado
        Retorna uma mensagem de confirmação da remoção.
    """

    candidato_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre candidato #{candidato_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando candidato
    candidato = session.query(Candidato).filter(Candidato.name == candidato_nome).first()
    
    if not candidato:
        error_msg = "Candidato não encontrado na base :/"
        logger.warning(f"Erro ao deletar candidato '{candidato_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(candidato)
        session.commit()
        logger.debug(f"Deletado candidato #{candidato_nome}")
        return {"message": f"Candidato {candidato_nome} removido com sucesso!"}, 200