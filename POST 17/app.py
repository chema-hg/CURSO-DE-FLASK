from flask import Flask, request, make_response
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def inicio():
    return '<h1>Esta es la página inicial</h1>'

@app.route('/set_cookie/')
def save_cookie():
    # make_response = La respuesta será 
    respuesta=make_response('Hemos guardado la cookie')
    # en respuesta ira la cooki 'nombre' 'la cookie en si'
    respuesta.set_cookie('galleta','Estoy guardado en el navegador', secure=True, httponly=True)
    return respuesta

@app.route('/set_cookie5m/')
def save_cookie5m():
    '''pone una cookie durante 5 minutos'''
    # make_response = La respuesta será 
    respuesta=make_response('Hemos guardado la cookie')
    # en respuesta ira la cookie 'nombre' 'la cookie en si'
    # max_age = 60 * 60 * 24 * 365; max_age va en segundos.
    respuesta.set_cookie('galleta','Estoy guardado en el navegador', secure=True, max_age=60*5)
    return respuesta

@app.route('/set_cookie90d/')
def save_cookie90d():
    '''Pone una cookie en vigor durante 90 dias'''
    # make_response = La respuesta será 
    respuesta=make_response('Hemos guardado la cookie')
    # en respuesta ira la cookie 'nombre' 'la cookie en si'
    # expires = usando un objeto de datetime.
    final = datetime.datetime.now()
    final = final + datetime.timedelta(days=90)
    respuesta.set_cookie('galleta','Estoy guardado en el navegador', secure=True, expires=final)
    return respuesta

@app.route('/set_cookie24092021')
def save_cookie90dunix():
    '''Pone una cookie en vigor durante 90 dias'''
    # make_response = La respuesta será 
    respuesta=make_response('Hemos guardado la cookie')
    # en respuesta ira la cookie 'nombre' 'la cookie en si'
    # expires = usando tiempo unix para que la cookie expire el 24092021.
    final = datetime.datetime.now()
    final = final + datetime.timedelta(days=90)
    respuesta.set_cookie('galleta','Estoy guardado en el navegador', secure=True, expires=1632488124)
    return respuesta

@app.route('/get_cookie/')
def read_cookie():
    leer_galleta = request.cookies.get('galleta')
    return f'El contenido de la cookie es: {leer_galleta}'

@app.route('/get_cookie1/')
def read_cookie1():
    '''por si usas el atributo path="/get_cookie/" y quieres ver como solo se puede leer
    la cookie desde ese path y no desde este'''
    leer_galleta = request.cookies.get('galleta')
    return f'El contenido de la cookie es: {leer_galleta}'

if __name__=="__main__":
    app.run(debug=True)