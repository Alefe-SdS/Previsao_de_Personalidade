# 🧠 Classificador de Personalidade com Machine Learning

O objetivo deste projeto é desenvolver um modelo preditivo baseado em aprendizado de máquina para classificar perfis de 
personalidade (introvertido e extrovertido) a partir de dados sociais. Utilizando um conjunto de dados com variáveis como 
frequência de postagens, participação em eventos e cansaço após socialização, o projeto passou pelas etapas de limpeza de dados, 
codificação de à análise de características variáveis categóricas, normalização, divisão entre treino e teste, e 
aplicação do algoritmo K-Nearest Neighbors (KNN). O modelo obteve uma acurácia de praticamente 92,18% na validação. 
comportamentais, essa tecnologia permite observar informações como hábitos sociais ou preferências individuais e, a partir disso,  
O sistema foi exportado via Pickle e integrado a uma interface desenvolvida com Flask bibliotecas da linguagem python. Os 
resultados mostram que é possível prever perfis comportamentais com base em interações sociais e características pessoais. 
Palavras-chave: Machine Learning Personalidade; Python; KNN; Flask. 

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **KNN (scikit-learn)**: Algoritmo de machine learning
- **Matplotlib**: Visualização gráfica dos dados
- **Pickle**: Serialização do modelo treinado
- **Flask**: Framework web para interface do usuário
-  **HTML & CSS**: Interface do usuário

## 📊 Funcionalidades

- Análise e visualização dos dados com gráficos
- Treinamento de modelo com KNN
- Salvamento do modelo com Pickle
- Interface web interativa para preenchimento de dados
- Previsão em tempo real com Flask + HTML + CSS
  
A aplicação prevê traços de personalidade com base em um conjunto de dados sociais O modelo é treinado com o algoritmo **KNN** e os dados processados com **pandas**. A previsão é feita por meio de uma interface web simples, com o modelo carregado via **pickle**.

## 🏗️ Estrutura do Projeto
```bash
📁 ML/
│
├── venv/ # Ambiente virtual Python
│
├── dados/ # Arquivos de dados brutos
│ └── personalit_dataset.csv
│
├── notebook/ # Notebooks e scripts principais
│ ├── app.py # Backend Flask da aplicação
│ ├── atividadefinal.ipynb # Análise exploratória e modelagem
│ └── personalidade.pkl # Modelo treinado com pickle
│
├── templates/ # Páginas HTML da interface
│ ├── index.html # Formulário de entrada
│ └── resultado.html # Exibição do resultado da previsão
```
## 🚀 Como Executar o Projeto
  
1. Execute o app Flask:
```bash
Abrir um novo terminal e selecionar 'git bash' e depois digitar o comando abaixo:

ALEFE@DESKTOP-PFBKURH MINGW64 ~/Documents/ML
$ cd notebook (Para entrar na pasta notebook)

ALEFE@DESKTOP-PFBKURH MINGW64 ~/Documents/ML/notebook
$ python app.py (Para executar o app flask)
```
2. Acesse no navegador:
```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000 (Link Para acessar no navegador )
```

3. Para Sair
```bash
Digitar no terminal **CTRL+C** para sair
```

## 💻 Interface Web

A interface é composta por um formulário em HTML, onde o usuário insere suas informações sociais. O backend (Flask) processa os dados e retorna a previsão dos traços de personalidade na página ```resultado.html ```.

## 📈 Análise de Dados
O arquivo ```atividadefinal.ipynb ``` contém a análise exploratória com visualizações em ```matplotlib```, além do treinamento e validação do modelo KNN.

## 👤 Autores (GitHub)
- [Álefe Santana dos Santos](https://github.com/Alefe-SdS/)
- [Sarah da Costa Silva Lira](https://github.com/Esdraspenha)
- [Esdras Penha](https://github.com/)



 



