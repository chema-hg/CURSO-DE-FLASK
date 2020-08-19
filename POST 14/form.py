from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
# Si un campo tiene que ser opcional hay que decirlo especificamente
from wtforms.validators import DataRequired, Email, Optional


class Crear_Registro(FlaskForm):
    nombre = StringField('Nombre del empleado', validators=[DataRequired()])
    correo = StringField('Correo Electrónico', validators=[Email("Correo Electrónico no Válido")])
    telefono = IntegerField('Número de Telefono', validators=[Optional()])
    enviar = SubmitField('Enviar')