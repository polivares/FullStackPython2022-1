# Paso 1: agregamos la biblioteca Flask
from flask import Flask

# A partir de la clase Flask, crearemos una instancia de la clase
app = Flask(__name__) # en la variable app tengo un objeto de la clase Flask

# Utilizando el decorador, indicamos a Flask
# 1) Que esta es una función a utilizar por Flask
# 2) La ruta en que se verá esta página
@app.route("/")
def hola():
    return "<h1>Hola mundo!</h1>"

if __name__=="__main__":
    # Esta línea ejecuta la aplicación
    app.run(debug=True)
