class Player:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def win_money(self, amount):
        self.money += amount

        