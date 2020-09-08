from flask import Flask
app=Flask(__name__)

@app.route('/')
def inicio():
    return "hola Mundo"

@app.route('/acerca_de/')
def acercade():
    return "Pagina editada por Perico Perez"

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return 'Pues no he encontrado la página....'

if __name__=='__main__':
    app.run(debug=True)

