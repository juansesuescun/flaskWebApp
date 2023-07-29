#Creacion de database models
# importar db object de esta misma carpeta
from . import db
# modulo de flask que nos ayuda a hacer login
from flask_login import UserMixin
#modulo para traer func que es basicamente para la fecha, se ingresa un dato a la base de datos y automaticamente le da la fecha actual
from sqlalchemy.sql import func

#Esquema general de la base de datos
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #Asociacion de diferente informacion con diferentes usuarios
    # one to many - un usuario a muchas notas
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class User(db.Model, UserMixin):
    #Aqui se define que va a tener la base de datos, columnas 
    # con su identificador tipo de dato y id es primary key
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')
