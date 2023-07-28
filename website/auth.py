from flask import Blueprint, render_template

# definicion de blueprint para autenticacion o login
auth = Blueprint('auth', __name__)


#Definiendo las rutas para login logout
@auth.route('/login')
def login():
    return render_template("login.html", text = "Testing", user = "Juanse")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")