''' Código de los formularios

Recogerá todas las clases de los formularios'''
from flask_wtf import FlaskForm
# Importamos los campos que necesitamos
from wtforms import StringField, PasswordField, BooleanField
# Importamos los validadores
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
import inicio


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
                               InputRequired(), Length(min=8, max=50, message='Longitud mínima de 8 caracteres y máxima de 50')])
    # El maximo de 80 en la longitud de la contraseña es porque posteriormente la codificaremos
    # con un algoritmo sha-256
    contrasena2 = PasswordField('Repite la Contraseña', validators=[
                                InputRequired(), EqualTo('contrasena', message='Las contraseñas no coinciden.')])
    # Usamos este campo contrasena2 para verificar que el usuario introduce la contraseña correcta.

    # Definimos nuestros propios validadores usando la estructura validate_<nombre_del_campo>
    # Validador para comprobar que el nombre de usuario no este ya registrado
    def validate_nombre_usuario(self, nombre_usuario):
        user = inicio.Usuario.query.filter_by(
            nombre_usuario=nombre_usuario.data).first()
        if user is not None:
            raise ValidationError(
                'Por favor, utiliza un nombre de usuario diferente.')

    # Validador para comprobar que el correo electronico no esté registrado.
    def validate_correo_electronico(self, correo_electronico):
        user = inicio.Usuario.query.filter_by(
            correo_electronico=correo_electronico.data).first()
        if user is not None:
            raise ValidationError(
                'Por favor, usa una dirección de correo electrónico distinta.')
