from .form import Formulario_de_Login, Formulario_de_Registro
from flask import redirect, url_for, request, render_template, flash
# Por temas de seguridad en la ruta
from werkzeug.urls import url_parse
# para que la contraseña no se guarde como texto plano
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from flask_login import current_user, login_user, logout_user, login_required
from inicio import db
from .modelos import Usuario


# Vista para iniciar sesión en el sistema
@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = Formulario_de_Login()
    # (2) Si el usuario ya estuviera registrado no tiene sentido que volviera a hacer un login
    # asi que lo mandamos de vuelta a la página del dashboard
    if current_user.is_authenticated:
        return redirect(url_for('private.dashboard'))
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
                    next_page = url_for('private.dashboard')
                return redirect(next_page)
                # return redirect(url_for('dashboard')) sustituido por lo anterior
        # Si el usuario no existe o la contraseña es incorrecta
        # return "<h2>Usuario o Contraseña incorrecta</h2>"
        flash('El usuario no existe o la contraseña es incorrecta')
        return redirect(url_for('auth.login'))    
    else:
        return render_template('login.html', form=form)


# Vista para registrarse o añadir un usario al sistema
@auth.route('/signup/', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = Formulario_de_Registro()
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

# Para terminar creamos un sistema de log-out
@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.home'))
