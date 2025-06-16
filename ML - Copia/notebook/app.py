from flask import Flask, request, render_template
import os
import pickle
import numpy as np

# Caminho absoluto para a pasta templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route("/resultado.html")
def resultado():
    return render_template("resultado.html")


# Carrega o modelo salvo (ajuste o nome do arquivo se necessário)
with open("personalidade.pkl", "rb") as f:
    modelos = pickle.load(f)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prever", methods=["POST"])
def prever():
    try:
        dados = request.get_json()

        Medo_de_palco_Yes = 1 if dados['Medo_de_palco'] == 'Sim' else 0
        Cansaco_social = 1 if dados['Cansaco_pos_socializacao_Yes'] == 'Sim' else 0

        entrada = np.array([[ 
            float(dados['Tempo_sozinho']),
            float(dados['Participacao_evento_social']),
            float(dados['Sair_de_casa']),
            float(dados['Tamanho_grupo_amigos']),
            float(dados['Frequencia_posts']),
            Medo_de_palco_Yes,
            Cansaco_social,
        ]])
        print("Entrada recebida:", entrada)

        predicao = modelos.predict(entrada)[0]
        return {"personalidade": predicao}
    
    except Exception as e:
        return {"erro": str(e)}, 400


if __name__ == '__main__':
    app.run(debug=True)
