from flask import render_template
from . import public

@public.route('/')
def home():
    return render_template('pagina_inicial.html')