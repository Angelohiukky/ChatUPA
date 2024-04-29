from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Get the user's name and problem from the form
        nome = request.form["Seu nome, por favor"]
        problema = request.form["Conta qual o problema"]

        # Store the information in the database (implementation needed)

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

    # Return the list of responses
    return respostas

# Function to create the table in the database (already executed)
def criar_tabela():
    # ... (implementation as provided in the original code)

# Create the table if it doesn't exist (only run once)
criar_tabela()

if __name__ == "__main__":
    app.run(debug=True)