from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=["GET"])
def calculadora_get():
    if request.method == "GET" and len(request.args) == 0:
        return render_template("formulario_get.html")
    else:
        primer_numero = int(request.args.get('primer_numero'))
        segundo_numero = int(request.args.get('segundo_numero'))
        operacion = request.args.get('operacion')
        try:
            if operacion == "+":
                resultado = primer_numero + segundo_numero
            elif operacion == "-":
                resultado = primer_numero - segundo_numero
            elif operacion == "*":
                resultado = primer_numero * segundo_numero
            else:
                resultado = primer_numero / segundo_numero
            return render_template("formulario_get.html", resultado=resultado)
        except:
            return "No se ha podido realizar la operación"


if __name__ == "__main__":
    app.run(debug=True)
