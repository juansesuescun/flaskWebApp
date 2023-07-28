# setup de la aplicacion en flask
from flask import Flask

def create_app():
    #inicializacion de la app
    app = Flask (__name__)

    # Con esta variable se encripta o se asegura, las cookies y session data, esto en produccio no se debe mostrar pero bueno este es por la prueba
    app.config['SECRET_KEY'] = 'asffa asdf'

    #regitro de las rutas en este archivo
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app

