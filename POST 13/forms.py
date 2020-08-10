# Importamos FlaskForm
from flask_wtf import FlaskForm
# Por dependencia instala wtform de donde cojemos los campos que necesitemos.
from wtforms import SubmitField, FileField
# importamos el validador para que el campo sea obligatorio de rellenar.
from wtforms.validators import DataRequired

class subir_archivo(FlaskForm):
    # nombre_campo = TipoField('Etiqueta (label)', validadores=[])
    campo_subir = FileField('Subir Imagen', validators=[DataRequired()])
    enviar = SubmitField()
    

    