from flask import Flask
from app.models.animal import Animal
from app.models.enclosure import Enclosure
from app.models.visitors import Visitors
from app.models.player import Player
from app.models.zoo import Zoo



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

def get_an_animal_felicidade():
    lion_enclosure = Enclosure(name="Savana Africana", species="Leão").get_an_animal_felicidade("Simba")

    return lion_enclosure

def ganhar_dinheiro():
    ganhou = Zoo.receive_visitor_for_a_unique_enclousure("Savana Africana", "Simba", "Leão")

    return ganhou


if __name__ == "__main__":
    meu_web_app.run()
