from flask import Flask
# Importaremos la clase Grupo para obtener información desde la base de datos
from grupo import Grupo

app = Flask(__name__)

@app.route('/listagrupos')
def index():
    grupos = Grupo.get_all()
    print("Lista grupos:", grupos)
    un_grupo = Grupo.get('Primer grupo')
    print("Un grupo:", un_grupo)
    return '<h1>Listado de grupos</h1>'

@app.route('/insertargrupo/<string:nombre_grupo>/<string:descripcion_grupo>/')
def insertar(nombre_grupo, descripcion_grupo):
    data = {
        'nombre_grupo': nombre_grupo,
        'descripcion_grupo': descripcion_grupo
    }
    print(data)
    un_grupo = Grupo.save(data)
    print("Un grupo:", un_grupo)
    return '<h1>Insertar grupo</h1>'

if __name__ == '__main__':
    app.run(debug=True)
