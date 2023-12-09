from model.test.avaliador import Avaliador
from model.test.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/Admission_Predict_Test.csv"
colunas = ['greScore', 'toeflScore', 'universityRating', 'statementPurpose', 'letterRecomendation', 'undergraduateGPA', 'researchExperience', 'chanceOfAdmit']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1] 
 
# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/AdmissionPredictKNN.pkl'
    modelo_knn = Model.carrega_modelo(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn = avaliador.avaliar(modelo_knn, X, Y)
    
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.6