''' Código de los formularios

Recogerá todas las clases de los formularios'''

from flask_wtf import FlaskForm
# Importamos los campos que necesitamos
from wtforms import StringField, PasswordField, BooleanField
# Importamos los validadores
from wtforms.validators import InputRequired, Email, Length

# ----------------------- Creamos las clases de los formularios -----------------------------


class Formulario_de_Login(FlaskForm):
    # va a tener 3 campos nombre_usuario, contrasena y recuerdame
    # Nombre_usario es un campo de texto, necesario y con una longitud minima de 4 y max de 15 caracteres
    nombre_usuario = StringField('Nombre de Usuario', validators=[
                                 InputRequired(), Length(min=4, max=15)])
    # Campo contrasena
    contrasena = PasswordField('Contraseña', validators=[
                               InputRequired(message='Campo obligatorio'), Length(min=8, max=80)])
    # Campo recuerdame es un checkbox
    recuerdame = BooleanField('Recuérdame')


class Formulario_de_Registro(FlaskForm):
    nombre_usuario = StringField('Nombre de Usuario', validators=[
                                 InputRequired(), Length(min=4, max=15)])
    correo_electronico = StringField('Correo Electrónico', validators=[
                                     InputRequired(), Email(message="Email no válido"), Length(max=50)])
    contrasena = PasswordField('Contraseña', validators=[
                               InputRequired(), Length(min=8, max=80)])
    # El maximo de 80 en la longitud de la contraseña es porque posteriormente la codificaremos
    # con un algoritmo sha-256
