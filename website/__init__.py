# setup de la aplicacion en flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Setup de base de datos
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #inicializacion de la app
    app = Flask (__name__)

    # Con esta variable se encripta o se asegura, las cookies y session data, esto en produccio no se debe mostrar pero bueno este es por la prueba
    app.config['SECRET_KEY'] = 'asffa asdf'

    # Necesitamos decirle a flask que estamos usando esa db y donde esta localizada
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # ahora inicializamos la base de datos
    db.init_app(app)
    # definimos la base de datos , el esquema


    #regitro de las rutas en este archivo
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app

