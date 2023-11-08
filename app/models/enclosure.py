from animal import Animal
class Enclosure:
    def __init__(self, name, species, well_maintained=True):

        self.name = name
        self.species = species
        self.animals = []
        self.well_maintained = well_maintained

    def criar_recinto(self, name, species):
        recinto = Enclosure(self, name, species)
        return recinto
    
    def get_an_animal_felicidade(self, name):
        felicidade = Animal.verifica_felicidade(self, name)
        return felicidade

    def add_animal(self, animal):
        if animal.species != self.species:
            raise ValueError(f"Este recinto só aceita animais da espécie {self.species}.")
        
        self.animals.append(animal)

    def good_maintain(self):
        self.well_maintained = True

    def bad_maintain(self):
        self.well_maintained = False