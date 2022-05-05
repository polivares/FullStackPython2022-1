from pokeinfo import app
from flask import render_template, request, jsonify
import requests

@app.route('/pokemon', methods=['GET'])
def search():
    pokemon = request.args.get('pokemon')
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    response = requests.get(url)
    return response.json()

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')