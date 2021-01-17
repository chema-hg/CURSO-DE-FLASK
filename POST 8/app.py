from flask import Flask, request
app=Flask(__name__)

@app.route("/")
def inicio():
    return "pagina de inicio"

@app.route("/info/", methods=["GET","POST"])
def info():
    if request.method=="POST":
        usuario = request.form.get("minombre")
        return f"Has accedido usando el método Post, {usuario}"
    if request.method=="GET":
        return f'''
    <p><strong>request.url:</strong> La URL a la que accedemos.--> {request.url}</p>
    <p><strong>request.path:</strong>  La ruta de la URL, quitamos el servidor y los parámetros con la información. --> {request.path}</p>
    <p><strong>request.method:</strong>  El método HTTP con el que hemos accedido. --> {request.method}</p>
    <p><strong>request.headers:</strong>  Las cabeceras de la petición HTTP. --> {request.headers}</p>
    <p><strong>request.form:</strong>  Información recibida en el cuerpo de la petición con el método POST. --> {request.form}</p>
    <p><strong>request.args:</strong>  Parámetros con información indicado en la URL en las peticiones GET. --> {request.args}</p>
    <p><strong>request.files:</strong>  Ficheros para subir al servidor en una petición PUT o POST. --> {request.files}


<form action="/info/" method="POST">
        <hr/>
        <label> Introduce tu nombre </label>
        <input type="text" name="minombre">
        <strong> Al pulsar enviar accederás a la vista con el metodo POST </strong>
        <input type="submit" value="Enviar"/>
</form>'''

if __name__=="__main__":
    app.run(debug=True)