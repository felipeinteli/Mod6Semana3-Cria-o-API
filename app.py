from flask import Flask
from app.models.animal import Animal
from app.models.enclosure import Enclosure

meu_web_app = Flask('meu_web_app')

@meu_web_app.route('/create_animal', methods=['POST'])
def create_animal():
    lion = Animal(name="Simba", species="Leão")

@meu_web_app.route('/create_enclosure', methods=['POST'])

def create_enclosure():
    lion_enclosure = Enclosure(name="Savana Africana", species="Leão")

@meu_web_app.route('/add_animal_to_enclosure', methods=['POST'])
def add_animal_to_enclosure():
    lion_enclosure.add_animal(Simba)


if __name__ == "__main__":
    meu_web_app.run()
