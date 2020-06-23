# Autor: Alan Hergenreder

import random
from src.bingo import generador_bingo
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    color = ['Gold','LawnGreen','OrangeRed','Teal','SaddleBrown','Indigo','HotPink','SeaGreen','DarkRed']
    t = generador_bingo()
    return render_template("plantilla.html",talonario=t,color=color[random.randrange(9)])
