from flask import Blueprint, render_template

# recomendacion: poner el mismo nombre a la variable que el archivo o directorio que contenga
# el Blueprint
segunda = Blueprint("segunda", __name__, static_folder="static", template_folder="templates")
# static _folder y template_folder son opcionales

@segunda.route('/')
@segunda.route('/home/')
def home():
    return render_template('home.html')


