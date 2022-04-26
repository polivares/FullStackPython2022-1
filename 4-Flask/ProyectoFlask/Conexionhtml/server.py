from flask import Flask, render_template

app = Flask(__name__)

usuarios = [] # Variable global que almacena el listado de usuarios

@app.route('/bienvenido/<string:nombre>/<string:email>')
def welcome(nombre, email):
    nuevo_usuario = {'nombre': nombre, 'email': email}
    usuarios.append(nuevo_usuario) # Cada vez que se llama la función welcome, agrego un usuario
    return render_template('bienvenido.html', usuarios=usuarios)

if __name__ == '__main__':
    # Ejecución de la aplicación flask
    app.run(debug=True)