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
    # x_old = x_new
    # y_old = y_new
    # z_old = z_new
    x_new = request.form['x']
    y_new = request.form['y']
    z_new = request.form['z']
    # x_deslocamento = x_old - x_new
    # y_deslocamento = y_old - y_new
    # z_deslocamento = z_old - z_new
    coord = Coordenada(x_db = x_new, y_db = y_new, z_db = z_new)
    session.add(coord)
    session.commit()
    return render_template("index.html", x_new=x_new, y_new=y_new, z_new=z_new)

if __name__ == "__main__":
    app.run(debug=True)