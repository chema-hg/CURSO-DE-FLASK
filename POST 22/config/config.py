import os

# token de seguridad
SECRET_KEY = '42651a92d21bbc54ee5daa264295aa4d49b535c2'

# directorio de trabajo
PWD = os.path.abspath(os.curdir)

# depurador on
DEBUG = False

# Base de datos
# Cadena de conexion
SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') or f'sqlite:///{PWD}/base_de_datos/dbase.db'
# Desactivar mensajes de SQLALCHEMY
SQLALCHEMY_TRACK_MODIFICATIONS = False
# from_object solo tiene en cuenta los nombres de los parametros puestos en 
# mayusculas