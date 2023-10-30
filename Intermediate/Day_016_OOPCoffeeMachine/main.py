# OOP Coffee Machine
#  A software version of a coffee machine using object-oriented programming

from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


def main():
    # Initialize components
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True
    while is_on:
        command = input(f"What would you like? ({menu.get_items()}): ").lower()
        if command == "off":
            # Turn off the coffee machine
            is_on = False
        elif command == "report":
            # Report on storage of coffee and money machines
            coffee_machine.report()
            money_machine.report()
        elif (order := menu.find_drink(command)) is not None:
            # Process valid order
            if coffee_machine.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_machine.make_coffee(order)
        else:
            # Unrecognized command
            print(f"'{command}' is not a beverage available.")


if __name__ == "__main__":
    main()
