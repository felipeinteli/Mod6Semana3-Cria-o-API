class Animal:
    def __init__(self, name=None, species=None, happiness_level=50, felicidade=True):
        self.name = name
        self.species = species
        self.happiness_level = happiness_level
        self.felicidade = felicidade

    def __str__(self):
        return f"Animal(Name: {self.name}, Species: {self.species}, Happiness Level: {self.happiness_level})"

    def feed(self, food_amount):
        self.happiness_level += food_amount
        
        return self.happiness_level

    def verifica_felicidade(self):
        if self.happiness_level > 50:
            self.felicidade = True
            return self.felicidade
        else:
            self.felicidade = False
            return self.felicidade
        
# simba = Animal(name="Simba", species="Leão")
