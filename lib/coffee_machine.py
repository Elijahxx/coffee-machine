import random


class CoffeeMachine:
    def __init__(self):
        self.beans = 200
        self.cups = 10
        self.water = 2500
        self.milk = 1000
        self.money = 0

    def _is_full(self):
        return (
            self.beans == 200
            and self.cups == 10
            and self.water == 2500
            and self.milk == 1000
        )

    def fill(self):
        if self._is_full():
            return "Already full, sir!"
        else:
            self.beans = 200
            self.cups = 10
            self.water = 2500
            self.milk = 1000
            return "Thanks, sir. I'm full now!"

    def withdraw_money(self):
        money = self.money
        messages = [
            "Successfully withdrawed {} dollars!".format(money),
            "Sending {} dollars to the charity!".format(money),
            "Bying crypto on all {} dollars!".format(money),
        ]
        if money > 0:
            self.money = 0
            return random.choice(messages)
        else:
            return "Nothing to withdraw, sir. Buy yourself some coffee!"

    def _has_ingredients(self, drink):
        status = (
            self.beans >= drink["beans"]
            and self.water >= drink["water"]
            and self.milk >= drink["milk"]
            and self.cups > 0
        )
        return status

    def brew(self, drink):
        ok = self._has_ingredients(drink)
        if ok:
            print("Good choice, sir")
            self.beans -= drink["beans"]
            self.water -= drink["water"]
            self.milk -= drink["milk"]
            self.cups -= 1
            self.money += drink["price"]
            return "Your {} is ready. Have a nice day!".format(drink["name"])
        else:
            return "Can't make you a drink. Fill the machine!"
