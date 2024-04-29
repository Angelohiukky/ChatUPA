import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Obter nome, problema e setor do formulário
        nome = request.form["nome"]
        problema = request.form["problema"]
        setor = request.form["setor"]

        # Connect to the database
        conexao = sqlite3.connect("chat.db")
        cursor = conexao.cursor()

        # Insert the user's information into the 'respostas' table
        cursor.execute("INSERT INTO respostas (nome, problema, setor) VALUES (?, ?, ?)", (nome, problema, setor))

        conexao.commit()

        # Close the database connection
        conexao.close()

        # Display a message to the user
        return render_template("index.html", mensagem="Valeu, já vamos resolver!!!")

@app.route("/respostas")
def mostrar_respostas():
    # Connect to the database
    conexao = sqlite3.connect("chat.db")
    cursor = conexao.cursor()

    # Fetch all responses from the 'respostas' table
    cursor.execute("SELECT * FROM respostas")
    respostas = cursor.fetchall()

    # Close the database connection
    conexao.close()

    # Render the responses in the 'respostas.html' template
    return render_template("respostas.html", respostas=respostas)


# Function to create the table in the database (already executed)
def criar_tabela():
    conexao = sqlite3.connect("chat.db")
    cursor = conexao.cursor()

    # ... (implementação para criação da tabela como no código original)

    conexao.commit()
    conexao.close()

criar_tabela()

if __name__ == "__main__":
    app.run(debug=True)
