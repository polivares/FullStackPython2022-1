# Paso 1: agregamos la biblioteca Flask
from flask import Flask

# A partir de la clase Flask, crearemos una instancia de la clase
app = Flask(__name__) # en la variable app tengo un objeto de la clase Flask

# Utilizando el decorador, indicamos a Flask
# 1) Que esta es una función a utilizar por Flask
# 2) La ruta en que se verá esta página
@app.route("/")
@app.route('/index')
def hola():
    return "<h1>Hola mundo!</h1>"

# Agregaremos dos rutas, una para la descripción de mi página y otra para
# los contactos (oficina y personal)

@app.route('/description/')
@app.route('/descripcion/')
def description():
    return '<h1>Soy una empresa muy bonita</h1>'


@app.route('/contact/<contact_type>/<int:id>')
def contact(contact_type, id):
    if contact_type == 'office':
        return f'Usuario id {id}: Mis datos de oficina son +1111111111' 
    elif contact_type == 'personal':
        return f'Usuario id {id}: Mis datos personales son... personales'
    else:
        return 'Datos incorrectos'




# # Decorador para manejo de error 404 
# # (página no encontrada/Page not found!)
# @app.errorhandler(404)
# def url_error(e):
#     return e

if __name__=="__main__":
    # Esta línea ejecuta la aplicación
    app.run(debug=True)
