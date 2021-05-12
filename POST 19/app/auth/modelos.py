from flask_login import UserMixin
from inicio import db

# --------------------------------- Modelo de bases de datos------------------------

# Hay que modificar la clase usuario para trabajar con la clase UserMixin de Flask-login


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(15), unique=True)
    correo_electronico = db.Column(db.String(50), unique=True)
    contrasena = db.Column(db.String(94))


# ----------------------------------------------------------------------------------
