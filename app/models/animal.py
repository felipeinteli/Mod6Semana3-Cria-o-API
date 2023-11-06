class Animal:
    def __init__(self, name, species, happiness_level=50):
        self.name = name
        self.species = species
        self.happiness_level = happiness_level

    def feed(self, food_amount):
        self.happiness_level += food_amount
        self.happiness_level = min(self.happiness_level, 100)