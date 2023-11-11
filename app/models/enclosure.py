from app.models.animal import Animal
from typing import List

class Enclosure:
    def __init__(self, name, species, well_maintained=True):

        self.name = name
        self.species = species
        self.animals: List[Animal] = []
        self.well_maintained = well_maintained

    def __str__(self):
        return f"Enclosure(Name: {self.name}, Species: {self.species}, Well Maintained: {self.well_maintained}, Animals: {self.animals})"

    def add_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise TypeError("O objeto deve ser uma instância de Animal")
        
        # Verificando se a espécie do animal corresponde à espécie do recinto
        if animal.species != self.species:
            raise ValueError(f"Este recinto só aceita animais da espécie {self.species}. Espécie fornecida: {animal.species}")

        self.animals.append(animal)
    
    def is_well_maintained(self):
        return self.well_maintained

    def good_maintain(self):
        self.well_maintained = True

        return self.well_maintained

    def bad_maintain(self):
        self.well_maintained = False

        return self.well_maintained 