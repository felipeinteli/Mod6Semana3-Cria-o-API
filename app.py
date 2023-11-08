from flask import Flask
from app.models.animal import Animal
from app.models.enclosure import Enclosure


meu_web_app = Flask('meu_web_app')

def create_animal():
    animal = Animal.criar_animal("Simba", "Leão")

    return animal

def feed_animal():
    lion = Animal(name="Simba", species="Leão")
    lion.feed(50)

    return lion.happiness_level

def criar_recinto():
    lion_enclosure = Enclosure(name="Savana Africana", species="Leão")

    return lion_enclosure

def add_animal_to_enclosure():
    lion_enclosure = Enclosure(name="Savana Africana", species="Leão").add_animal(Animal(name="Simba", species="Leão"))

    return lion_enclosure

def cuidar_bem_recinto():
    lion_enclosure = Enclosure(name="Savana Africana", species="Leão").good_maintain

    return lion_enclosure

def cuidar_mal_recinto():
    lion_enclosure = Enclosure(name="Savana Africana", species="Leão").bad_maintain

    return lion_enclosure



if __name__ == "__main__":
    meu_web_app.run()
