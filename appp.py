
from app.models.animal import Animal
from app.models.enclosure import Enclosure
from app.models.visitors import Visitor
from app.models.player import Player

from app.models.zoo import Zoo

class Appp:
    def __init__(self):
        self.player = Player("João")
        self.visitor = Visitor("João", 10000)
        self.animal = Animal("Simba", "Leão")
        self.lion_enclosure = Enclosure(name="Savana Africana", species="Leão")
        self.zoo = Zoo("Zoológico de São Paulo", self.player)
        self.visitor = Visitor("João", 10000)

    # def create_animal(self):
    #     self.animal = Animal("Simba2", "Leão")
    #     print("animal", self.animal)
    #     return self.animal
    
    def add_animal_to_enclosure(self):
        self.lion_enclosure.add_animal(self.animal)
        print("animais no enclosure")
        for animal in self.lion_enclosure.animals:
            print(animal) 
        return self.lion_enclosure.animals

    def feed_animal(self):
        self.animal.feed(50)
        print("happiness_level", self.animal.happiness_level)
        return self.animal.happiness_level

    def add_enclosure_to_zoo(self):
        self.zoo.add_enclosure(self.lion_enclosure)
        print("enclosures do zoo", self.zoo.enclosures)
        return self.zoo.enclosures

    def cuidar_bem_recinto(self):
        if self.lion_enclosure:
            self.lion_enclosure.good_maintain()
            print("well_maintained", self.lion_enclosure.well_maintained)
        return self.lion_enclosure

    def insert_visitor(self):
        self.zoo.add_visitor(Visitor("João", 100))
        print("visitantes do zoo", self.zoo.visitors)
        return self.zoo.visitors

    def cuidar_mal_recinto(self):
        if self.lion_enclosure:
            self.lion_enclosure.bad_maintain()
            print("well_maintained", self.lion_enclosure.well_maintained)
        return self.lion_enclosure

    def get_an_animal_felicidade(self):
        if self.animal:
            self.animal.verifica_felicidade()
            print("felicidade", self.animal.felicidade)
        return self.animal.felicidade

    def ganhar_dinheiro(self):
        self.zoo.receber_visitantes(10)
        print("money", self.player.money)
        return self.player.money


# if __name__ == "__main__":
#     app = Appp()

#     # Chamando os métodos
#     app.add_animal_to_enclosure()
#     # app.create_animal()
#     app.feed_animal()
#     app.add_enclosure_to_zoo()
#     app.cuidar_mal_recinto()
#     app.cuidar_bem_recinto()
#     app.insert_visitor()
#     app.get_an_animal_felicidade()
#     app.ganhar_dinheiro()