
from app.models.animal import Animal
from app.models.enclosure import Enclosure

from app.models.zoo import Zoo

class Appp:
    def __init__(self):
        self.lion_enclosure = None  # Initialize enclosure

    def create_animal(self):
        animal = Animal("Simba", "Leão")

        return animal

    def feed_animal(self):
        lion = Animal(name="Simba", species="Leão")
        lion.feed(50)

        return lion.happiness_level

    def criar_recinto(self):
        self.lion_enclosure = Enclosure(name="Savana Africana", species="Leão")

        return self.lion_enclosure

    def add_animal_to_enclosure(self):
        self.lion_enclosure.add_animal(Animal(name="Simba", species="Leão"))

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
        if self.lion_enclosure:
            return self.lion_enclosure.get_an_animal_happiness("Simba")
        return None

    def ganhar_dinheiro(self):
        ganhou = Zoo.receive_visitor_for_a_unique_enclosure("Savana Africana", "Simba", "Leão")
        return ganhou


