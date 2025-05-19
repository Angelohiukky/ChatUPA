from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Pegar o nome do usuário e o problema
        nome = request.form["Seu nome, por favor"]
        problema = request.form["Conta qual o problema"]

        # Guardar a informação no banco de dados (necessário implementar)

        return render_template("index.html", mensagem="Valeu, já vamos resolver!!!")

@app.route("/respostas")
def mostrar_respostas():
    # conectar com a database
    conexao = sqlite3.connect("chat.db")
    cursor = conexao.cursor()

    # obter as respostas da tabela 'respostas'
    cursor.execute("SELECT * FROM respostas")
    respostas = cursor.fetchall()

    # fechar a conexão com database
    conexao.close()

    # Retornar lista de respostas
    return respostas

# Função para criar uma tabela na database (já executado)
def criar_tabela():

# Criar a tebela se ela não existir (Apenas uma vez)
criar_tabela()

if __name__ == "__main__":
    app.run(debug=True)
