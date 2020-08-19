import os

# token de seguridad
SECRET_KEY = '42651a92d21bbc54ee5daa264295aa4d49b535c2'

# directorio de trabajo
PWD = os.path.abspath(os.curdir)

# servidor con depurador
DEBUG = True

# Cadena de conexión a la base de datos
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/database/dbase.db'.format(PWD)
# gestion de notificaciones de sqlalchemy desactivada.
SQLALCHEMY_TRACK_MODIFICATIONS = False
