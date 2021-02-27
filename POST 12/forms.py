# Importamos la extensión FlaskForm que nos permitirá usar wtform
from flask_wtf import FlaskForm
# Definimos los diferentes campos que vamos a utilizar
from wtforms import IntegerField, SelectField, SubmitField, StringField, BooleanField, DateField
from wtforms import RadioField, PasswordField, TextAreaField
# Definimos los validadores
from wtforms.validators import DataRequired, Optional

# Creamos la clase formulario_calculadora que heredará de FlaskForm
class formulario_calculadora(FlaskForm):
    # Definimos cada uno de los campos
    primer_numero = IntegerField("Número 1", validators=[DataRequired('Tienes que introducir un número entero')])
    segundo_numero = IntegerField("Número 2", validators=[DataRequired('Tienes que introducir un número entero')])
    operacion = SelectField("Operación", choices=[
        ('+', 'Sumar'),
        ('-', 'Restar'),
        ('*', 'Multiplicar'),
        ('/', 'Dividir')
    ])
    enviar = SubmitField('Botón Enviar')