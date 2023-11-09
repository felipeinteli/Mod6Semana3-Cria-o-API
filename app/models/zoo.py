from animal import Animal
from enclosure  import Enclosure
from visitors import Visitor
# from player import Player
class Zoo:

    def __init__(self, name):
        self.name = name
        self.list_visitors = {}
        self.list_enclosures = {}
        self.list_animals = {}

    def insere_visitors(self, visitor):
        self.list_visitors[visitor.name] = visitor
        return self.list_visitors
    
    def insere_enclosures(self, enclosure):
        self.list_enclosures[enclosure.name] = enclosure
        return self.list_enclosures 

    def insere_animals(self, animal):
        self.list_animals[animal.name] = animal
        return self.list_animals

    def receive_visitor_for_a_unique_enclosure(self, enclosure_name, animal_name, amount):
        enclosure = self.list_enclosures.get(enclosure_name)
        animal = self.list_animals.get(animal_name)
        if enclosure and animal:
            if enclosure.good_maintain() and animal.verifica_felicidade() == "O animal está feliz":
                # Presumindo que Visitor.gastar_dinheiro é um método que faz algo com o valor amount
                Visitor.gastar_dinheiro(amount)  # Isso parece estranho, pois Visitor é uma classe e não uma instância
                return "O visitante teve uma experiência agradável."
            else:
                return "O visitante não teve uma experiência agradável."
        return "Recinto ou animal não encontrado."

    # def visitante_entrou_zoologico(self, name):
    #     visitor = Visitor(name=name)
    #     self.receive_visitor_for_a_unique_enclousure(visitor)
    #     return visitor
            
