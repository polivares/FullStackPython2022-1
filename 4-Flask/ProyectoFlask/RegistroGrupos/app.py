from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "esta es mi llave"

grupos = [] # Esta variable almacena una lista, donde cada elemento es un grupo

@app.route('/')
@app.route('/register')
def register():
    if len(grupos) == 0:
        id = 1
    else:
        id = grupos[-1].id + 1
    return render_template("register.html", id=id)

@app.route('/agrega_grupo', methods=['POST'])
def add_group():
    if request.method == "POST":
        if len(grupos) == 0: # Si es el primer grupo a registrarse
            id = 1 # Pongo id en 1
        else: # Sino es el primer grupo
            id = grupos[-1].id + 1 # El id es igual al último
        integrante1 = request.form.get("integrante1")
        integrante2 = request.form.get("integrante2")
        integrante3 = request.form.get("integrante3")
        integrantes = [integrante1, integrante2, integrante3]
        tema = request.form.get("project_title")
        descripcion = request.form.get("project_description")
        group = Grupo(id, integrantes, tema, descripcion)
        grupos.append(group)
        return redirect("/lista_grupos")
    else:
        return redirect("/")


@app.route('/lista_grupos', methods=["GET"])
def list_groups():
    return render_template("list_groups.html", grupos=grupos)
        
    
class Grupo:
    def __init__(self, id, integrantes, tema, descripcion):
        self.id = id
        self.integrantes = integrantes
        self.tema = tema
        self.descripcion = descripcion


if __name__ == '__main__':
    app.run(debug=True)
