from src.bingo import generador_bingo
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    t = generador_bingo()
    return render_template("plantilla.html",talonario=t)
