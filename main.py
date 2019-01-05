import os

from pyfiglet import Figlet
from lib.coffee_machine import CoffeeMachine
from lib.drinks import drinks


f = Figlet(font='slant')
title = "\nWelcome to\n" + f.renderText("Python Coffee!")


def greet():
    print("\033[H\033[J")
    print(title)


def wait_action():
    return input("Press [Enter] to continue...")


def make_coffee(machine):
    greet()
    print("Choose your beverage wisely, we have like three of them!")
    options = ["Espresso", "Latte", "Cappucino", "Back"]
    for i, option in enumerate(options):
        print("[" + str(i + 1) + "] " + option)

    choice = int(input("Enter your choice [1-4]: ")) - 1
    if choice in range(0, 3):

        message = machine.brew(drinks[choice])
        print(message)
        input("Press [Enter] to continue...")
    elif choice == 3:
        return
    else:
        print("I don't know this drink, sir!")
        wait_action()

def fill_machine(machine):
    message = machine.fill()
    print(message)
    wait_action()


def withdraw_money(machine):
    message = machine.withdraw_money()
    print(message)
    wait_action()


def show_data(machine):
    greet()
    print("At your service, sir!")
    print("Beans: {}".format(machine.beans))
    print("Water: {}".format(machine.water))
    print("Cups: {}".format(machine.cups))
    print("Money: {}".format(machine.money))
    wait_action()


def show_main_menu():
    greet()
    options = ["Make coffee", "Fill the machine", "Withdraw money", "Show data", "Exit"]
    for i, option in enumerate(options):
        print("[" + str(i + 1) + "] " + option)


machine = CoffeeMachine()
loop = True
while loop:
    show_main_menu()
    try:
        choice = int(input("Enter your choice [1-5]: "))
        if choice in range(1, 6):
            if choice == 1:
                make_coffee(machine)
            if choice == 2:
                fill_machine(machine)
            if choice == 3:
                withdraw_money(machine)
            if choice == 4:
                show_data(machine)
            if choice == 5:
                loop = False
                exit()
        else:
            print("Indeed, sir!")
            wait_action()
    except ValueError:
        print("I don't speak this language, sir!")
        wait_action()
