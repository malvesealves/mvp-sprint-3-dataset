from sklearn.metrics import accuracy_score

class Avaliador:

    def avaliar(self, modelo, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Podendo parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = modelo.predict(X_test)
        return (accuracy_score(Y_test, predicoes))
    