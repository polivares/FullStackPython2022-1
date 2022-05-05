from flask import Flask
import requests

app = Flask(__name__)

@app.route('/pokemon/<string:pokemon>')
def pokemon(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    response = requests.get(url)
    return response.json()

if __name__=='__main__':
    app.run(debug=True)