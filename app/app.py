from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Index'

@app.route("/info")
def info():
    """
    La libreria request sirve para obtener peticiones
    y en este caso, hacemos una peticion de los argumentos
    que vienen por la ruta, se envian despues del signo (?)
    con el formato clave=valor
    por ejemplo localhost:5000/info?pag=1&can=10
    argumento pag 1 y valor 10
    """
    argumentos = request.args
    if argumentos != {}:
        return argumentos
    return 'No hay argumentos'

#DEVOLVEMOS UN HTML
#IMPORTAR EL METODO RENDER_TEMPLATE DE LA LIBRERA FLASK, Y CREAMOS UN TEMPLATE
#(home.html)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/parametros")
def parametros():
    lista_nombres = ['Juan', 'Pedro', 'Ana', 'Maria']
    return render_template('parametros.html', nombres=lista_nombres)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
