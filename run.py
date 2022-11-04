# Autor: Alan Hergenreder

from src.bingo import generador_bingo
from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def index():
    t = generador_bingo()
    return render_template("index.html", bingo = t)
