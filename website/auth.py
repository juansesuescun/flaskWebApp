from flask import Blueprint

# definicion de blueprint para autenticacion o login
auth = Blueprint('auth', __name__)


#Definiendo las rutas para login logout
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"