from flask import Flask, render_template

app = Flask(__name__)

# Vista inicial, se puede entrar directamente o
# introducir un nombre como parámetro
@app.route("/")
@app.route("/<nombre>/")
def inicio(nombre=None):
    return render_template("inicio.html", nombre=nombre)

# Vista de la página Uno
@app.route("/pagina_uno/")
def paginaUno():
    return render_template("pagina_uno.html")

# Vista de la página Sobre Nosotros
@app.route('/sobre_nosotros/')
def sobreNosotros():
    return render_template('sobre_nosotros.html')


if __name__ == "__main__":
    app.run(debug=True)
