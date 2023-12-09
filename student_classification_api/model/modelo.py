import numpy as np
import pandas as pd
import pickle
from logger import logger
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


class Model:

    def carrega_modelo(path):
        """Carrega o modelo pkl
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um candidato com base no modelo treinado
        """
        X_input = np.array([form.greScore, 
                            form.toeflScore, 
                            form.universityRating, 
                            form.statementPurpose, 
                            form.letterRecomendation, 
                            form.undergraduateGPA, 
                            form.researchExperience
                        ])
        # Realiza o reshape para que o modelo entenda que estamos passando
        prediction = model.predict(X_input.reshape(1, -1))
        return int(prediction[0])


    