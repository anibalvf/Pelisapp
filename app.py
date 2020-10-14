from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from Scraper import *

app = Flask(__name__)
Bootstrap(app)


lista = scrap()
@app.route('/')
def hello_world():

    return render_template("tables.html",peliculas=lista)