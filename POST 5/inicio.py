from flask import Flask, render_template
import datetime
app = Flask(__name__)

lista_nav = ['Inicio', 'Pagina_1', 'Acerca_de']


@app.route('/')
@app.route('/<nombre>/')
def inicio(nombre=None):
    if nombre == None:
        nombre = ""
    ahora = datetime.datetime.now()
    return render_template("plantilla_inicial.html", usuario=nombre, dia=ahora.day, mes=ahora.month, ano=ahora.year, lista_nav=lista_nav)


@app.route('/acerca_de/')
def acercade():
    return "Página editada por Perico Perez"


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "Pues no he encontrado la página...", 404


if __name__ == "__main__":
    app.run(debug=True)
