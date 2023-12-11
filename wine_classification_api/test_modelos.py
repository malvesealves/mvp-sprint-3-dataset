from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/winequality-red.csv"
colunas = ['fixedAcidity', 'volatileAcidity', 'citricAcid', 'residualSugar', 'chlorides', 'freeSulfurDioxide', 'totalSulfurDioxide', 'density', 'ph', 'sulphates', 'alcohol', 'quality']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar modelo KNN padronizado a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/winequality_knn_orig.pkl'
    modelo_knn = modelo.carrega_modelo(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn = avaliador.avaliar(modelo_knn, X, Y)
    
    # Testando as métricas do KNN padronizado
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.60
    