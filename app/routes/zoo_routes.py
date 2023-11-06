from flask import Blueprint, request, jsonify
from models.animal import Animal
from models.enclosure import Enclosure

zoo = Blueprint('zoo', __name__)

@zoo.route('/create_animal', methods=['POST'])
def create_animal():


@zoo.route('/create_enclosure', methods=['POST'])
def create_enclosure():

