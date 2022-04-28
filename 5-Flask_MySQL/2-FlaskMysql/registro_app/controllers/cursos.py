from registro_app import app
from registro_app.models.grupo import Grupo
from registro_app.models.integrante import Integrante
from flask import render_template, redirect, request, session


@app.route('/grupos')
def grupos():
    grupos = Grupo.get_all()
    print("Lista grupos:", grupos)
    un_grupo = Grupo.get('Primer grupo')
    print("Un grupo:", un_grupo)
    return '<h1>Listado de grupos</h1>'

@app.route('/insertargrupo/<string:nombre_grupo>/<string:descripcion_grupo>')
def insertargrupo(nombre_grupo, descripcion_grupo):
    data = {
        'nombre_grupo': nombre_grupo,
        'descripcion_grupo': descripcion_grupo
    }
    un_grupo = Grupo.save(data)
    print("Un grupo:", un_grupo)
    return '<h1>Insertar grupo</h1>'

@app.route('/')
@app.route('/register')
def register():
    grupos = Grupo.get_all()
    if len(grupos) == 0:
        id = 1
    else:
        id = grupos[-1].idGrupo + 1
    return render_template("register.html", id=id)

@app.route('/agrega_grupo', methods=['POST'])
def add_group():
    if request.method == "POST":
        grupos = Grupo.get_all()
        if len(grupos) == 0: # Si es el primer grupo a registrarse
            id = 1 # Pongo id en 1
        else: # Sino es el primer grupo
            id = grupos[-1].idGrupo + 1 # El id es igual al último
        data_grupo = {
            'idGrupo': id,
            'nombre_grupo': request.form.get("nombre_grupo"),
            'descripcion_grupo': request.form.get("project_description")
        }
        nuevo_grupo = Grupo.save(data_grupo)
        integrante1 = Integrante.save({'nombre_integrante':request.form.get("integrante1"),
                                        'idGrupo': nuevo_grupo.idGrupo})
        integrante2 = Integrante.save({'nombre_integrante':request.form.get("integrante2"),
                                        'idGrupo': nuevo_grupo.idGrupo})
        integrante3 = Integrante.save({'nombre_integrante':request.form.get("integrante3"),
                                        'idGrupo': nuevo_grupo.idGrupo})
        return redirect("/lista_grupos")
    else:
        return redirect("/")

@app.route('/lista_grupos', methods=["GET"])
def list_groups():
    grupos = Grupo.get_all()
    datos_grupos = []
    for grupo in grupos:
        data_grupo={
            'idGrupo': grupo.idGrupo
        }
        integrantes = Grupo.get_integrantes_by_group(data_grupo)
        datos_grupos.append({
            'idGrupo': grupo.idGrupo,
            'nombre_grupo': grupo.nombre_grupo,
            'descripcion_grupo': grupo.descripcion_grupo,
            'integrantes': integrantes
        })
    return render_template("list_groups.html", grupos=datos_grupos)