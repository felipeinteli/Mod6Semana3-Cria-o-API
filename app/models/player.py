class Player:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def __str__(self):
        return f"Player(Name: {self.name}, Money: {self.money})"

    def win_money(self, amount):
        self.money += amount

        