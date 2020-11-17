from flask import Flask
from flask import redirect, url_for, abort
app=Flask(__name__)

@app.route("/")
def inicio():
    return "Hola Mundo"

@app.route("/acerca_de/")
def acercaDe():
    return "Página editada por Perico Perez"

@app.errorhandler(404)
def pagina_no_encontrada(error):
# Hay que ponerle un parámetro a la función porque el decorador se lo pasa
# Retornaremos el mensaje que queramos y tambien devolveremos de nuevo el error
    return "Pues no he encontrado esa página....", 404

@app.route("/hola/")
@app.route("/hola/<nombre>/")
def bienvenida(nombre=None):
    if nombre:
        return f"Bienvenido a nuestra web, {nombre}"
    else:
        return "Hola usuario Anónimo"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1,num2):
    return f"la suma de {num1} más {num2} es: " + str(num1+num2)

# Va a ir a la vista bienvenida pasándole el párametro Antonio
@app.route("/ir_hola/")
def regreso():
    return redirect(url_for('bienvenida', nombre='Antonio'))

@app.route('/registro/')
def registro():
    return abort(401)

if __name__=="__main__":
    app.run(debug=True)