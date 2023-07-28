# Aqui se va a importar el package , traer la funcion 
from website import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)