from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calculadora_post():
    if request.method == "GET":
        return render_template("formulario_post.html")
    if request.method == "POST":
        primer_numero = int(request.form.get('primer_numero'))
        segundo_numero = int(request.form.get('segundo_numero'))
        operacion = request.form.get('operacion')
        try:
            if operacion == "+":
                resultado = primer_numero + segundo_numero
            elif operacion == "-":
                resultado = primer_numero - segundo_numero
            elif operacion == "*":
                resultado = primer_numero * segundo_numero
            else:
                resultado = primer_numero / segundo_numero
            return render_template("formulario_post.html", resultado=resultado)
        except:
            return "No se ha podido realizar la operación"  

if __name__== "__main__":
     app.run(debug=True)
            
