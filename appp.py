
from app.models.animal import Animal
from app.models.enclosure import Enclosure
from app.models.visitors import Visitor

from app.models.zoo import Zoo

class Appp:
    def __init__(self):
        self.animal = None
        self.lion_enclosure = None  # Initialize enclosure
        self.zoo = Zoo("Zoológico de São Paulo")
        self.zoo.insere_visitors(Visitor("João", 100))

    def create_animal(self):
        self.animal = Animal("Simba", "Leão")

        return self.animal

    def feed_animal(self):
        lion = Animal(name="Simba", species="Leão")
        lion.feed(50)

        return lion.happiness_level

    def criar_recinto(self):
        self.lion_enclosure = Enclosure(name="Savana Africana", species="Leão")

        return self.lion_enclosure

    def cuidar_bem_recinto(self):
        if self.lion_enclosure:
            self.lion_enclosure.good_maintain()
        return self.lion_enclosure

    def cuidar_mal_recinto(self):
        if self.lion_enclosure:
            self.lion_enclosure.bad_maintain()
        return self.lion_enclosure

    def get_an_animal_felicidade(self):
        if self.animal:
            self.animal.verifica_felicidade()
        return self.animal.felicidade

    def ganhar_dinheiro(self):
        ganhou = self.zoo.receive_visitor_for_a_unique_enclosure("Savana Africana", "Simba",  100)
        return ganhou


