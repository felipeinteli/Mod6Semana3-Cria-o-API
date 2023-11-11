
class Visitor:
    def __init__(self, name=None, money=1000000):
        self.name = name
        self.money = money
    
    def __str__(self):
        return f"Visitor(Name: {self.name}, Money: {self.money})"

    def gastar_dinheiro(self, amount):
        self.money -= amount
        
        return self.money
