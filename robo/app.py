import sqlite3 #importar para inciar o banco de dados no sqlite
from flask import Flask, render_template, redirect, request
from data.coordinate import Valores

app = Flask(__name__)

@app.route("/")
def index():
    db = sqlite3.connect("data/bank.db")
    box = db.cursor()
    box.execute("SELECT * FROM historico")
    dados = box.fetchall() #pegar tudo do banco e coloca na caixa. ORGANIZA O QUE TÁ DENTRO da tabela
    db.close()
    
    for posicao in range(len(dados)):
        dados[posicao] = Valores(
            x = dados[posicao][0],
            y = dados[posicao][1],
            z = dados[posicao][2]
            )
    
    
    return render_template("index.html", dados=dados)

@app.route("/valor", methods=["GET", "POST"])
def dados():
    if request.method == "POST":
        coordenadas = Valores(
            x = request.form["coordenada_x"],
            y = request.form["coordenada_y"],
            z = request.form["coordenada_z"] 
        )

        db = sqlite3.connect("data/bank.db")
        box = db.cursor()
        box.execute("INSERT INTO historico (coordenada_x, coordenada_y, coordenada_z) VALUES (?,?,?)", (coordenadas.x, coordenadas.y, coordenadas.z))
        db.commit()
        db.close()
        return redirect("/")
    
    


if __name__ == '__main__':
    app.run(debug=True) #O parâmetro debug=True é opcional e pode ser utilizado para exibir mensagens de erro detalhadas.