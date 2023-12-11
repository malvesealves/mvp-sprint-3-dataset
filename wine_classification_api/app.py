from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Vinho, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
vinho_tag = Tag(name="Vinho", description="Adição, visualização, remoção e predição da qualidade de vinhos")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de vinhos
@app.get('/vinhos', tags=[vinho_tag],
         responses={"200": VinhoViewSchema, "404": ErrorSchema})
def get_vinhos():
    """Lista todos os vinhos cadastrados na base
    Retorna uma lista de vinhos cadastrados na base.
    
    Args:
        nome (str): nome do vinho
        
    Returns:
        list: lista de vinhos cadastrados na base
    """
    session = Session()
    
    # Buscando todos os vinhos
    vinhos = session.query(Vinho).all()
    
    if not vinhos:
        logger.warning("Não há vinhos cadastrados na base :/")
        return {"message": "Não há vinhos cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d vinhos econtrados" % len(vinhos))
        return apresenta_vinhos(vinhos), 200


# Rota de adição de vinho
@app.post('/vinho', tags=[vinho_tag],
          responses={"200": VinhoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: VinhoSchema):
    """Adiciona um novo vinho à base de dados
    Retorna uma representação dos vinhos e diagnósticos associados.
    
    Args:
        name (str): nome do vinho
        preg (int): número de vezes que engravidou: Pregnancies
        plas (int): concentração de glicose no plasma: Glucose
        pres (int): pressão diastólica (mm Hg): BloodPressure
        skin (int): espessura da dobra cutânea do tríceps (mm): SkinThickness
        test (int): insulina sérica de 2 horas (mu U/ml): Insulin
        mass (float): índice de massa corporal (peso em kg/(altura em m)^2): BMI
        pedi (float): função pedigree de diabetes: DiabetesPedigreeFunction
        age (int): idade (anos): Age
        
    Returns:
        dict: representação do vinho e diagnóstico associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/diabetes_lr.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    vinho = Vinho(
        name=form.name.strip(),
        preg=form.preg,
        plas=form.plas,
        pres=form.pres,
        skin=form.skin,
        test=form.test,
        mass=form.mass,
        pedi=form.pedi,
        age=form.age,
        outcome=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando produto de nome: '{vinho.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se vinho já existe na base
        if session.query(Vinho).filter(Vinho.name == form.name).first():
            error_msg = "Vinho já existente na base :/"
            logger.warning(f"Erro ao adicionar vinho '{vinho.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando vinho
        session.add(vinho)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado vinho de nome: '{vinho.name}'")
        return apresenta_vinho(vinho), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar vinho '{vinho.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de vinho por nome
@app.get('/vinho', tags=[vinho_tag],
         responses={"200": VinhoViewSchema, "404": ErrorSchema})
def get_vinho(query: VinhoBuscaSchema):    
    """Faz a busca por um vinho cadastrado na base a partir do nome

    Args:
        nome (str): nome do vinho
        
    Returns:
        dict: representação do vinho e diagnóstico associado
    """
    
    vinho_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{vinho_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinho = session.query(Vinho).filter(Vinho.name == vinho_nome).first()
    
    if not vinho:
        # se o vinho não foi encontrado
        error_msg = f"Vinho {vinho_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{vinho_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Vinho econtrado: '{vinho.name}'")
        # retorna a representação do vinho
        return apresenta_vinho(vinho), 200
   
    
# Rota de remoção de vinho por nome
@app.delete('/vinho', tags=[vinho_tag],
            responses={"200": VinhoViewSchema, "404": ErrorSchema})
def delete_vinho(query: VinhoBuscaSchema):
    """Remove um vinho cadastrado na base a partir do nome

    Args:
        nome (str): nome do vinho
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    vinho_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre vinho #{vinho_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando vinho
    vinho = session.query(Vinho).filter(Vinho.name == vinho_nome).first()
    
    if not vinho:
        error_msg = "Vinho não encontrado na base :/"
        logger.warning(f"Erro ao deletar vinho '{vinho_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(vinho)
        session.commit()
        logger.debug(f"Deletado vinho #{vinho_nome}")
        return {"message": f"Vinho {vinho_nome} removido com sucesso!"}, 200