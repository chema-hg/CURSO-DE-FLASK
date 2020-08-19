from flask import Flask, render_template, redirect, url_for
# parametros o configuración de la aplicacion
import config
# importamos sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# importamos la clase del formulario
from form import Crear_Registro

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# -------------------------- Modelos de la base de datos ----------------------------


class Empleados(db.Model):
    '''Tabla de datos de los empleados de la empresa'''
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    correo = db.Column(db.String(30), unique=True, nullable=False)
    telefono = db.Column(db.Integer)

    def __repr__(self):
        # cuando se represente el objeto quedara mas legible
        return f'<Empleado {self.nombre}>'

# ------------------------- Rutas -----------------------------------------

# Ruta principal de la aplicacion
@app.route('/')
def home():
    # Devuelve todos los registros de la tabla Empleados en forma de objeto
    empleados = Empleados.query.all()
    return render_template('main.html', empleados=empleados)

# Ruta para crear un nuevo registro
@app.route('/create/', methods=["GET", "POST"])
def create_item():
    form = Crear_Registro()
    if form.validate_on_submit():
        # empleado es una instancia de la clase Empleado
        empleado = Empleados(
            nombre=form.nombre.data,
            correo=form.correo.data,
            telefono=form.telefono.data)
        try:
            db.session.add(empleado)
            db.session.commit()
            return redirect(url_for('home'))
        except:
            return 'ha habido un problema en la creación de un nuevo empleado'
    else:
        return render_template('create.html', form=form)

# Ruta para actualizar un registro ya existente
@app.route('/update/<int:id>', methods=["GET", "POST"])
def update_item(id):
    empleado = Empleados.query.filter_by(id=id).first()
    form = Crear_Registro(nombre=empleado.nombre,
                          correo=empleado.correo, telefono=empleado.telefono)
    if form.validate_on_submit():
        empleado = Empleados.query.get(id)
        empleado.nombre = form.nombre.data
        empleado.correo = form.correo.data
        empleado.telefono = form.telefono.data
        try:
            db.session.commit()
            return redirect(url_for('home'))
        except:
            return 'Ha habido un error en la actualización del empleado {}' .format(id)

    else:
        return render_template('update.html', form=form, id=id)

# Ruta para borrar un registro
@app.route('/delete/<int:id>/')
def delete_item(id):
    empleado = Empleados.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('home'))

# Ruta por si la vista no existe
@app.errorhandler(404)
def page_not_found(error):
    return "pagina no encontrada", 404


if __name__ == '__main__':
    app.run()
