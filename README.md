# MVP Sprint 3 - Pós-Graduação em Engenharia de Software
Repositório do MVP da Sprint 3 da Pós-Graduação em Engenharia de Software na PUC-Rio

---

## Conteúdo

Neste repositório são disponibilizados os seguintes conteúdos relativos ao projeto desenvolvido:

- Notebook (Google Colab) contendo o processo de criação do modelo de _machine learning_. O notebook pode ser encontrado no [link](https://colab.research.google.com/drive/1tfvosFF_qT-ACnfLy3NHU0pjtJ67A3nc) ou pode ser aberto ao acessar o arquivo NOTEBOOK_MVP_SPRINT3.ipynb disponibilizado no presente repositório;
- Dataset nomeado como '_Red Wine Quality_' utilizado como fonte de dados e encontrado na fonte [Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009);
- Pasta "Data CSV Files" com o _dataset_ usado;
- Diretórios e arquivos referentes às aplicações back e front, respectivamente, para fazer a carga do arquivo do modelo de machine learning e possibilitar a entrada de novos dados para que o modelo de classificação faça a predição da classe de saída e exibir o resultado na tela.

# Tema
O presente projeto tem por objetivo classificar a qualidade de variantes de vinhos tintos do rótulo português "Vinho Verde" de acordo com o arbitrado para o atributo qualidade do vinho a seguir:

- _Good wine_ (bom vinho): qualidade do vinho >= 7;

- _Not good wine_ (não bom vinho): qualidade do vino < 7;

> __Foi feito tratamento nos dados originais do _dataset_ para respeitar a assertiva acerca da classificação do vinho como um bom vinho (1) e como um não bom vinho (0), logo, o parâmetro _quality_ de valores iniciais variando entre 0 e 10 dará lugar aos possíveis valores 0 e 1.__

O _dataset_ utilizado possui os seguintes 12 atributos de entrada, baseados em propriedades físico-químicas, e suas breves explicações:
- _name_ (nome): nome atribuído à cada amostra de vinho para manipulação dos dados;

- _fixed acidity_ (acidez fixa): composto pela maioria dos ácidos envolvidos com vinho, fixos ou não voláteis (não evaporam facilmente);

- _volatile acidity_ (acidez volátivel): quantidade de ácido acético no vinho, na qual a níveis muito altos pode levar a um gosto desagradável;

- _citric acid_ (ácido cítrico): encontrado em pequenas quantidades, ácido cítrico pode adicionar refrescância e sabor aos vinhos;

- _residual sugar_ (açúcar residual): quantidade de açúcar remanascente depois dos descansos de fermentação;

- _chlorides_ (cloretos): quantidade de sais no vinho;

- _free sulfur dioxide_ (dióxido de enxofre livre): forma livre de SO2 existente entre SO2 molecular (como gás dissolvido) e íon bissulfito;

- _total sulfur dioxide_ (dióxido de enxofre total): quantidade de SO2 livre e vinculado;

- _density_ (densidade): a densidade do vinho é próxima da densidade da água dependendo do percentual de álcool e açúcar contido;

- _pH_ (pH): descreve quão ácido ou básico o vinho é numa escala de o (muito ácido) até 14 (muito básico);

- _sulphates_ (sulfatos): um aditivo do vinho que pode contribuir os níveis de gás dióxido de enxofre;

- _alcohol_ (álcool): percentual de álcool contido no vinho.

E 1 atributo de saída, baseado em dados sensoriais:

- _quality_ (qualidade): qualidade do vinho, avaliada com notas entre 0 e 10 (originalmente) e notas 0 ou 1 (pós tratamento)

---

## Como executar API e o Front da aplicação _Wine Classification_

Requisitos da API:
- Instalar as libs listadas no arquivo `requirements.txt`.
- É recomendado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

1 - Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo:
```
cd mvp-sprint-3-dataset\wine_classification_api
```

2 - Instalar Virtualenv
```
$ pip install VirtualEnv
```

3 - Criar Virtualenv
```
$ VirtualEnv venv
```

4 - Ativar venv
```
$ venv/scripts/activate
```

5 - Instalar libs python
```
(venv)$ pip install -r requirements.txt
```

6 - Executar API:
```
(venv)$ flask run --host 0.0.0.0 --port 5000
```

Em caso de modificações no código enquanto a API estiver rodando, utilizar o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Após seguir todos os passos, abrir o link abaixo no bavegador para verificar o status da API em execução
- [http://localhost:5000/#/](http://localhost:5000/#/)

Link para Documentação:
- [http://127.0.0.1:5000/openapi/]

## Como executar o Front

Basta fazer o download do projeto e abrir o arquivo _index.html_ no seu browser.

---
## Critério e execução da classe de Teste

O critério de validação a ser considerado será a acurária do modelo KNN padronizado escolhido. Para implementar a classe de teste, foi criada a assertiva de acurária maior ou igual a 60% para aprovação do teste e do seu respectivo modelo.

Foram utilizados os dados disponibilizados no _dataset_ tratado para conjunto de teste.

Instruções para execução:

1 - Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo:

```
cd pucrio-mvp-sprint3-dataset-master\predict_api
```

2 - Executar o comando abaixo para obter o resultado do Teste com a metodologia de classificação KNN
```
$ pytest
```

