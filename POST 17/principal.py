from flask import Flask
# importamos el blueprint
from app.admin.segunda import segunda

app=Flask(__name__)
# Lo registramos una vez creada la aplidación principal
app.register_blueprint(segunda, url_prefix="/admin/")

@app.route('/')
def test():
    return "<h1>Prueba</h1>"

if __name__=="__main__":
    app.run(debug=True)