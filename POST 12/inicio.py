from flask import Flask, render_template, request
# Importamos la clase formulario calculadora
from forms import formulario_calculadora

app=Flask(__name__)
# Clave de Cifrado del Formulario
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/", methods=["GET","POST"])
def calculadora_post():
    # Instanciamos un objeto llamado form de la clase formulario_calculadora
    # print(request.form) si queremos ver lo que envia el formulario.
    form = formulario_calculadora()
    if form.validate_on_submit():
        primer_numero = int(form.primer_numero.data)
        segundo_numero = int(form.segundo_numero.data)
        operacion = form.operacion.data
        try:
            if operacion=="+":
                resultado=primer_numero+segundo_numero
            elif operacion=="-":
                resultado=primer_numero-segundo_numero
            elif operacion=="*":
                resultado=primer_numero*segundo_numero
            else:
                resultado=primer_numero/segundo_numero
            return render_template("formulario_post.html", form=form, resultado=resultado)
            
        except:
            return "no se ha podido realizar la operacion"
    else:
        return render_template("formulario_post.html", form = form)

if __name__=="__main__":
    app.run(debug=True)