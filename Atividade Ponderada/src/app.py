from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.coordenada import Coordenada

# Setando o Banco de Dados
engine = create_engine("sqlite+pysqlite:///atividade_ponderada.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


# Rotas
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/coordenada", methods = ["POST"])
def coordenada():

    # Recebendo informaçõe sno formulário
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']

    coord = Coordenada(x_db = x, y_db = y, z_db = z)
    session.add(coord)
    session.commit()
    return render_template("index.html", x_new=x, y_new=y, z_new=z)

@app.route("/godot", methods = ["GET", "POST"])
def godot():

    # Fazendo requisições pro db e retornando pro front, para que o godot possa ler
    posicoes = session.query(Coordenada).all()
    
    x = posicoes[-1].x_db
    y = posicoes[-1].y_db
    z = posicoes[-1].z_db

    stringposicoes = f"{x},{y},{z}"

    return stringposicoes
    

if __name__ == "__main__":
    app.run(debug=True)