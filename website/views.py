# Rutas estandar para la app
from flask import Blueprint, render_template

# definicion de blueprint la llame views por comodidad
views = Blueprint('views', __name__)

#Definicion de ruta para pagina home
@views.route('/')
def home():
    return render_template("home.html")