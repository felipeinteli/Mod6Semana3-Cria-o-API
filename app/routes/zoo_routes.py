from flask import Blueprint, request, jsonify
from models.animal import Animal
from models.enclosure import Enclosure

zoo = Blueprint('zoo', __name__)

@zoo.route('/create_animal', methods=['POST'])
def create_animal():
    # Lógica para criar um animal
    pass

@zoo.route('/create_enclosure', methods=['POST'])
def create_enclosure():
    # Lógica para criar um recinto
    pass

# Continue com outros endpoints para alimentar animais, receber visitantes, etc.

# Não esqueça de registrar suas blueprints no app principal em app.py