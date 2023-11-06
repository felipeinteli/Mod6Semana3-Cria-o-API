class Enclosure:
    def __init__(self, name, species, well_maintained=True):

        self.name = name
        self.species = species
        self.animals = []
        self.well_maintained = well_maintained

    def add_animal(self, animal):
        if animal.species != self.species:
            raise ValueError(f"Este recinto só aceita animais da espécie {self.species}.")
        
        self.animals.append(animal)

    def maintain(self):
        self.well_maintained = True