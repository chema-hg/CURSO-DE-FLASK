from flask import Flask, make_response, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return 'Esta es la pagina inicial'


@app.route('/set_cookie/')
def save_cookie():
    respuesta = make_response({'nombre':'clave'})
    respuesta.set_cookie('mi_cookie', 'esto se guarda en la cookie')
    return respuesta


@app.route('/get_cookie/')
def read_cookie():
    leer_cookie = request.cookies.get('mi_cookie')
    return f'Contenido de la cookie -> {leer_cookie}'


if __name__ == '__main__':
    app.run(debug=True)
