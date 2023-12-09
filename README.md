# MVP Sprint 3 - Pós-Graduação em Engenharia de Software
Repositório do MVP da Sprint 3 da Pós-Graduação em Engenharia de Software na PUC-Rio

---

## Conteúdo

Neste repositório são disponibilizados os seguintes conteúdos relativos ao projeto desenvolvido:

- Notebook (Google Colab) contendo o processo de criação do modelo de _machine learning_. O notebook pode ser encontrado no [link](https://www.google.com/) ou pode ser aberto ao acessar o arquivo NOTEBOOK_MVP_SPRINT3.ipynb disponibilizado no presente repositório;
- Dataset nomeado como '_Students' Academic Performance Dataset_' utilizado como fonte de dados e encontrado na fonte [Kaggle](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data);
- Pasta "Data CSV Files" com o _dataset_ usado;
- Diretórios e arquivos referentes às aplicações back e front, respectivamente, para fazer a carga do arquivo do modelo de machine learning e possibilitar a entrada de novos dados para que o modelo de classificação faça a predição da classe de saída (B, M, L) e exibir o resultado na tela.

# Tema
O presente projeto tem por objetivo classificar o desempenho de estudantes em um dos três níveis marcados à seguir de acordo com as notas obtidas:

- _Low-Level_ (B - nível baixo): intervalo entre 0 e 69;

- _Middle-Level_ (M - nível médio): intervalo entre 70 e 89;

- _High-Level_ (L - nível alto): intervalo entre 90 e 100.

O _dataset_ utilizado possui os seguintes 16 atributos e seus respectivos valores possíveis:
- _Gender_ (gênero do estudante): (nominal: 'Male' ou 'Female’)

- _Nationality_ (nacionalidade do estudante): (nominal:’ Kuwait’,’ Lebanon’,’ Egypt’,’ SaudiArabia’,’ USA’,’ Jordan’,’
Venezuela’,’ Iran’,’ Tunis’,’ Morocco’,’ Syria’,’ Palestine’,’ Iraq’,’ Lybia’)

- _Place of birth_ (local de nascimento do estudante): (nominal:’ Kuwait’,’ Lebanon’,’ Egypt’,’ SaudiArabia’,’ USA’,’ Jordan’,’
Venezuela’,’ Iran’,’ Tunis’,’ Morocco’,’ Syria’,’ Palestine’,’ Iraq’,’ Lybia’)

- _Educational Stages_ (grau de escolaridade ao qual o estudante pertence): (nominal: ‘lowerlevel’,’MiddleSchool’,’HighSchool’)

- _Grade Levels_ (níveis de nota obtida pelo estudante): (nominal: ‘G-01’, ‘G-02’, ‘G-03’, ‘G-04’, ‘G-05’, ‘G-06’, ‘G-07’, ‘G-08’, ‘G-09’, ‘G-10’, ‘G-11’, ‘G-12 ‘)

- _Section ID_ (turma ao qual o estudante pertence): (nominal:’A’,’B’,’C’)

- _Topic_ (tópico da disciplina): (nominal:’ English’,’ Spanish’, ‘French’,’ Arabic’,’ IT’,’ Math’,’ Chemistry’, ‘Biology’, ‘Science’,’ History’,’ Quran’,’ Geology’)

- _Semester_ (semestre letivo): (nominal:’ First’,’ Second’)

- _Parent responsible for student_ (parente responsável pelo estudante): (nominal:’mom’,’father’)

- _Raised hand_ (quantas vezes o estudante levantou a mão na sala de aula): (numeric:0-100)

- _Visited resources_ (quantas vezes o estudante visitou o conteúdo do curso): (numeric:0-100)

- _Viewing announcements_ (quantas vezes o estudante verificar novos anúncios): (numeric:0-100)

- _Discussion groups_ (quantas vezes o estudante participou de grupos de discussão): (numeric:0-100)

- _Parent Answering Survey_ (parente respondeu a pesquisa realizada pela escola ou não): (nominal:’Yes’,’No’)

- _Parent School Satisfaction_ (responsável satisfeito com a escola): (nominal:’Yes’,’No’)

- _Student Absence Days_ (número de dias faltosos para cada estudante): (nominal: above-7, under-7)

---
