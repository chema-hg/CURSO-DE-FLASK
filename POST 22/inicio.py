from flask import Flask
# importando el archivo de configuración externalizado en app
from config import config
from flask_bootstrap import Bootstrap
# importando base de datos: SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Usamos 6 elementos de FLaskLogin
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Usando Flask-Login
gestor_inicio_sesion = LoginManager(app)
# gestor_inicio_sesion.init_app(app) 
gestor_inicio_sesion.login_view = 'auth.login'
# gestor_inicio_sesion.init_app(app) esta comentada porque ya se habia creado la app.
# Entonces he puesto la 'app' dentro de los parentesis de gestor_inicio_sesion=LoginManager(app)
# init_app se usa si antes de crear la app hubieramos usado:
# gestor_inicio_sesion = LoginManager() 
# y despues de creada la app con app=Flask(__name__)
# gestor_inicio_sesion.init_app(app)

# Importando modelos Blueprint
from app.public import public
from app.auth import auth
from app.private import private

# registro de Blueprints
app.register_blueprint(public)
app.register_blueprint(auth)
app.register_blueprint(private)

# se podria poner en tambien en auth/routes.py 
from app.auth.modelos import Usuario
# cargador de Usuario - Flask login & clase Usuario
@gestor_inicio_sesion.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "La pagina seleccionada no existe", 404


if __name__ == "__main__":
    app.run()
