from flask import Flask, render_template
from forms import subir_archivo
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key='7e2062620aa6b7ee4c77b32703e3cf3bef0f8c47'

@app.route('/', methods=['GET','POST'])
def inicio():
    form = subir_archivo()
    if form.validate_on_submit():
        f=form.campo_subir.data
        nombre_fichero = secure_filename(f.filename)
        f.save(app.root_path+"/static/img/"+nombre_fichero)
        return "Imagen subida correctamente"
    else:
        return render_template('formulario_post.html', form=form)
    
if __name__=="__main__":
    app.run(debug=True)
    

