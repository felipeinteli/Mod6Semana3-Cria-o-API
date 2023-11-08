from app import add_visitor_to_zoo
from zoo import Zoo

class Visitor:
    def __init__(self, name=None, money=1000000):
        self.name = name

    def visitante_entrou_zoologico(self, name):
        visitor = Visitor(self, name)
        add_visitor_to_zoo(visitor)
        return visitor