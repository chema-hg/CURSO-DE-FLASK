from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
@app.route('/<nombre>/')
def inicio(nombre=""):
    return render_template("plantilla_inicial.html", nombre=nombre)

@app.route('/acerca_de/')
def acercade():
    return "Página editada por Perico Perez"

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "Pues no he encontrado la página...", 404 

if __name__=="__main__":
    app.run(debug=True)