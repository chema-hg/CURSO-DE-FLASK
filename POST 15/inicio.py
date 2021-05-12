from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
# importando clases de los formularios
import forms
# importando base de datos: SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# para que la contraseña no se guarde como texto plano
from werkzeug.security import generate_password_hash, check_password_hash
# Usamos 6 elementos de FLaskLogin
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user
# Por temas de seguridad en la ruta
from werkzeug.urls import url_parse


app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
db = SQLAlchemy(app)
# Usando Flask-Login


# --------------------------------- Modelo de bases de datos------------------------

# Hay que modificar la clase usuario para trabajar con la clase UserMixin de Flask-login


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(15), unique=True)
    correo_electronico = db.Column(db.String(50), unique=True)
    contrasena = db.Column(db.String(94))


# ----------------------------------------------------------------------------------

gestor_inicio_sesion = LoginManager(app)
# Si le queremos indicar cual es la aplicación principal gestor_inicio_sesion.init_app(app)
# y antes quedaria gestor_inicio_sesion = LoginManager()
gestor_inicio_sesion.login_view = 'login'

# cargador de Usuario - Flask login & clase Usuario


@gestor_inicio_sesion.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('pagina_inicial.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = forms.Formulario_de_Login()
    # (2) Si el usuario ya estuviera registrado no tiene sentido que volviera a hacer un login
    # asi que lo mandamos de vuelta a la página del dashboard
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if form.validate_on_submit():
        # En la Tabla usuario buscamos los registros filtrando por el
        # nombre de usuario que nos dan en el formulario y seleccionamos el primero
        # que supuestamente no se tiene que repetir ya que asi lo hemos dicho al crear la base.
        usuario = Usuario.query.filter_by(
            nombre_usuario=form.nombre_usuario.data).first()
        # Tambien se podria haber utilizado un metodo de Flask-Login
        # usuario = get_user(form.nombre_usuario.data)

        # Si el usuario existe
        if usuario:  # o tambien If usuario is not None:
            # Miramos si la contraña introducida en el login coincide con la existente en la base
            # de datos.
            # if usuario.contrasena == form.contrasena.data:
            # Cuando usamos la contraseña codificada para comparar se usa:
            if check_password_hash(usuario.contrasena, form.contrasena.data):
                login_user(usuario, remember=form.recuerdame.data)
                # Si es verdad ha acedido al sistema y puede ver la pagina dashboard
                # pero por seguridad tenemos que añadir este código.
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('dashboard')
                return redirect(next_page)
                # return redirect(url_for('dashboard')) sustituido por lo anterior
        # Si el usuario no existe o la contraseña es incorrecta
        # return "<h2>Usuario o Contraseña incorrecta</h2>"
        flash('El usuario no existe o la contraseña es incorrecta')
        return redirect(url_for('login'))
    else:
        return render_template('login.html', form=form)


@app.route('/signup/', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = forms.Formulario_de_Registro()
    if form.validate_on_submit():
        contrasena_cifrada = generate_password_hash(form.contrasena.data)
        nuevo_usuario = Usuario(
            nombre_usuario=form.nombre_usuario.data,
            correo_electronico=form.correo_electronico.data,
            contrasena=contrasena_cifrada
        )
        # No añadimos id porque lo creara automaticamente la base de datos
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            return '''<h2>Nuevo usuario creado con exito</h2>
            <a href="/">Volver<a/>'''
            # # podriamos ya dejar logeado al usuario y redirigirlo al dashboard
            # login_user(user, remember=True)
            # next_page = request.args.get('next', None)
            # if not next_page or url_parse(next_page).netloc != '':
            #     next_page = url_for('dashboard')
            # return redirect(next_page)
        except:
            return "<h2>Ha habido un problema en la creacion del registro</h2>"

        # return "<h2>"+form.nombre_usuario.data+" "+form.contrasena.data+" "+form.correo_electronico.data+"</h2>"
    else:
        return render_template("signup.html", form=form)


@app.route('/dashboard/')
# decorador para que no se pueda entrar en la vista si no estas logeado
@login_required
def dashboard():
    return '''<h2>Bienvenido {},esta es la pagina de control <br/> a la que se puede acceder 
    si estas registrado.</h2>
    <br />
    <a href="/">Volver</a> 
    '''.format(current_user.nombre_usuario)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "La pagina seleccionada no existe", 404


# Para terminar creamos un sistema de log-out
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()
