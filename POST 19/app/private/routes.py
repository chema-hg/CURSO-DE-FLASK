from . import private
from flask_login import login_required, current_user

@private.route('/dashboard/')
# decorador para que no se pueda entrar en la vista si no estas logeado
@login_required
def dashboard():
    return '''<h2>Bienvenido {}, esta es la pagina de control <br/> a la que se puede acceder 
    si estas registrado.</h2>
    <br />
    <a href="/">Volver</a> 
    '''.format(current_user.nombre_usuario)