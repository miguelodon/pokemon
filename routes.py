from flask import Blueprint, render_template, request, jsonify
from utils import obtener_informacion_pokemon

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html', pokemon=None) 

@main_routes.route('/pokemon', methods=['GET'])
def get_pokemon():
    name = request.args.get('name')
    pokemon = obtener_informacion_pokemon(name)
    return render_template('datos/_resultado.html', pokemon=pokemon)

@main_routes.route('/pokemonsElegir', methods=['GET'])
def elegir_pokemon():
    name = request.args.get('name')
    pokemonElegir = obtener_informacion_pokemon(name)
    return render_template('pokemonsElegir/_resultado_select.html', pokemonElegir=pokemonElegir)