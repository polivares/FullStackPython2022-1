from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<nombre>/<apellido>/<int:edad>')
def user(nombre, apellido, edad):
    # Acá deberíamos tener la conexión entre un html y el renderizado
    # La función render template busca el archivo html entregado como
    # parámetro de entrada dentro de la carpeta templates (ojo con eso)

    # Para lograr el comportamiento esperado (mostrar la información del usuario)
    # debemos, entregar esta información al archivo html a través del proceso
    # de renderizado.
    return render_template('user.html', name=nombre,
                           last_name=apellido,
                           age=edad)


# Ejemplo de repetición de texto
@app.route('/repeat/<int:num>/<string:texto>')
def repeat(num, texto):
    return render_template('repeat.html', num=num, texto=texto)

if __name__=='__main__':
    app.run(debug=True)