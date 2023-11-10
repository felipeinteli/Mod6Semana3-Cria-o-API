from app.models.player import Player

class Visitor:
    def __init__(self, name=None, money=1000000):
        self.name = name
        self.money = money

    def gastar_dinheiro(self, amount):
        self.money -= amount
        Player.win_money(amount)
        return self.money
