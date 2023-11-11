class Animal:
    def __init__(self, name=None, species=None, happiness_level=50, felicidade=True):
        self.name = name
        self.species = species
        self.happiness_level = happiness_level
        self.felicidade = felicidade

    def feed(self, food_amount):
        self.happiness_level += food_amount
        
        return self.happiness_level

    def verifica_felicidade(self):
        if self.happiness_level > 50:
            self.felicidade = True
            return self.felicidade
        else:
            return self.felicidade