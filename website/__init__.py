# setup de la aplicacion en flask
from flask import Flask

def create_app():
    #inicializacion de la app
    app = Flask (__name__)

    # Con esta variable se encripta o se asegura, las cookies y session data, esto en produccio no se debe mostrar pero bueno este es por la prueba
    app.config['SECRET_KEY'] = 'asffa asdf'

    return app