# Rutas estandar para la app
from flask import Blueprint

# definicion de blueprint la llame views por comodidad
views = Blueprint('views', __name__)

#Definicion de ruta para pagina home
@views.route('/')
def home():
    return "<h1>Test</h1>"