from flask import Blueprint, render_template, request, flash

# definicion de blueprint para autenticacion o login
auth = Blueprint('auth', __name__)


#Definiendo las rutas para login logout
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)< 4:
            flash('Email must be greater than 3 characters.', category = 'error')
        elif len(firstname) <2:
            flash('First Name must be greater than 1 character.', category = 'error')
        elif password1 != password2:
            flash('password don\'t match.', category = 'error')
        elif len(password1) <7:
            flash('password must be at least 7 characters.', category = 'error')
        else:
            # add user to database
            flash('account created', category='success')
    return render_template("sign_up.html")