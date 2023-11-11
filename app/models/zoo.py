from app.models.animal import Animal
from app.models.enclosure  import Enclosure
from app.models.visitors import Visitor
from app.models.player import Player
from typing import List


class Zoo:

    def __init__(self, name: str, player: Player):
        self.name = name
        self.player = player
        self.enclosures: List[Enclosure] = []
        self.visitors: List[Visitor] = []
    
    def __str__(self):
        return f"Zoo(Name: {self.name}, Enclosures: {self.enclosures}, Visitors: {self.visitors})"


    def add_enclosure(self, enclosure: Enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("O objeto deve ser uma instância de Enclosure")
        self.enclosures.append(enclosure)

    def add_visitor(self, visitor: Visitor):
        if not isinstance(visitor, Visitor):
            raise TypeError("O objeto deve ser uma instância de Visitor")
        self.visitors.append(visitor)

    def receber_visitantes(self, preco_por_visitante: float):
            # Supondo que 'total_visitantes' seja uma propriedade da classe Zoo
            total_visitantes = len(self.visitors)
            total_pagantes = total_visitantes

            for enclosure in self.enclosures:
                if not enclosure.is_well_maintained():
                    total_pagantes -= 1  # Subtrai um pagante por cada recinto mal mantido
                    continue

                for animal in enclosure.animals:
                    if not animal.verifica_felicidade():
                        total_pagantes -= 1  # Subtrai um pagante por cada animal infeliz

            # Garantindo que o total de pagantes não seja negativo
            total_pagantes = max(total_pagantes, 0)

            total_receita = total_pagantes * preco_por_visitante
            self.player.win_money(total_receita)

            return total_visitantes, total_pagantes, total_receita


            
