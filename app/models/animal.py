from app import add_animal_to_enclosure
from enclosure import Enclosure
class Animal:
    def __init__(self, name=None, species=None, happiness_level=50):
        self.name = name
        self.species = species
        self.happiness_level = happiness_level

    def criar_animal(self, name, species):
        animal = Animal(self, name, species)
        add_animal_to_enclosure(animal)
        return animal

    def feed(self, food_amount):
        self.happiness_level += food_amount
        self.happiness_level = min(self.happiness_level, 100)

    def verifica_felicidade(self):
        if self.happiness_level > 50:
            return "O animal está feliz"
        else:
            return "O animal está triste"