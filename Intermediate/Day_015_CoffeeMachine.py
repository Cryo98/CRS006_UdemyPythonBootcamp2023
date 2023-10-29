# COFFEE MACHINE PROGRAM
# Digital version of a coffee machine that dispenses hot beverages
# ===========================================================================
# Checklist
# TODO: (EXTRA) make it so that the menu shows only the available beverages
# TODO: (EXTRA) show price

from Day_015_CoffeeMachine_resources import MENU

# CONSTANTS
INITIAL_WATER = 300  # ml
INITIAL_MILK = 200  # ml
INITIAL_COFFEE = 100  # g
INITIAL_MONEY = 0  # $


def convert_menu_to_str(menu: dict) -> str:
    """Converts the items in the menu into a string

    Takes all the keys within the menu dictionary and combines them in a
    string with each element separated by a forward slash, the string is
    then returned.

    Parameters
    ----------
    menu : dict
        Dictionary with elements represented by keys having the name of the
        beverage

    Returns
    -------
    str
        A string containing all the keys from the menu separated by '/'
    """
    entries_text = ""
    for entry in menu:
        entries_text += entry
        entries_text += "/"
    entries_text = entries_text.removesuffix("/")
    return entries_text


def print_report(storage: dict) -> None:
    """Prints a report of the current storage of the machine

    Parameters
    ----------
    storage : dict
        Dictionary containing the amount of each stored item
    """
    water_amount = storage["water"]
    milk_amount = storage["milk"]
    coffee_amount = storage["coffee"]
    money_amount = storage["money"]
    print(f"Water: {water_amount} ml")
    print(f"Milk: {milk_amount} ml")
    print(f"Coffee: {coffee_amount} g")
    print(f"Money: ${money_amount}")


def check_resources(
        storage: dict,
        menu: dict,
        beverage: str,
        ) -> bool:
    """Check if the stored ingredients are sufficient

    Runs through the ingredients' amount necessary based on the beverage
    required by the user from the menu, and compares to the amount of that
    ingredient stored in the storage dictionary.
    It will return a flag equals to True if all ingredients are available,
    equal to False if any ingredient is not sufficient and print which is
    not sufficient.

    Parameters
    ----------
    storage : dict
        Dictionary containing the amounts of each ingredient stored using as
        a key the name of the ingredient.
    menu : dict
        Dictionary containing as keys all the beverages available, and each
        beverage containing a dictionary with all the ingredients as keys and
        their amount needed.
    beverage : str
        Lowercase string containing the name of the beverage selected.

    Returns
    -------
    bool
        Flag returning 'True' if all ingredients are available, 'False' if any
        ingredient is not sufficient.
    """
    ingredients_necessary = menu[beverage]["ingredients"]
    for ingredient in ingredients_necessary:
        if storage[ingredient] < ingredients_necessary[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins() -> float:
    """Prompt the user for coins

    Asks the user for the amount of different types of coins, and returning the
    total amount of money inserted.

    Returns
    -------
    float
        Total amount of dollars inserted
    """
    print("Please insert coins.")
    total_amount = 0
    quarters_amount = int(input("How many quarters?: "))
    total_amount += 0.25 * quarters_amount
    dimes_amount = int(input("How many dimes?: "))
    total_amount += 0.1 * dimes_amount
    nickels_amount = int(input("How many nickels?: "))
    total_amount += 0.05 * nickels_amount
    pennies_amount = int(input("How many pennies?: "))
    total_amount += 0.01 * pennies_amount
    return total_amount


def check_transaction(
        beverage: str,
        menu: dict,
        money_inserted: float,
        ) -> bool:
    """Checks that the transaction is successful

    Compares the amount of money inserted with the cost of the beverage
    selected from the menu, and returns a Flag signaling if the transaction
    has been successful.
    Also prints messages connected to the result.

    Parameters
    ----------
    beverage : str
        Lowercase string containing the name of the selected beverage.
    menu : dict
        Dictionary containing all the available beverages, each containing
        their cost using the 'cost' keyword.
    money_inserted : dict
        Amount of dollars inserted by the user.

    Returns
    -------
    bool
        True if the money added was enough to buy the beverage, else False."""
    cost_beverage = menu[beverage]["cost"]
    if cost_beverage > money_inserted:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif money_inserted > cost_beverage:
        change = money_inserted - cost_beverage
        print(f"Here is ${change:.2f} dollars in change.")
    return True


def update_storage(
        beverage: str,
        menu: dict,
        storage: dict,
        ) -> None:
    """Updates the storage based on the beverage ordered.

    Extracts the ingredients and the cost for the selected beverage from the
    menu, removing the ingredients from the storage and incrementing the money
    by the cost amount.

    Parameters
    ----------
    beverage : str
        Lowercase string containing the name of the selected beverage.
    menu : dict
        Dictionary containing as keys all the beverages available, and each
        beverage containing a dictionary with all the ingredients as keys and
        their amount needed, and the cost as 'cost'.
    storage : dict
        Dictionary containing the amounts of each ingredient stored using as
        a key the name of the ingredient, and the amount of money stored as
        'money'.
    """
    ingredients_needed = menu[beverage]["ingredients"]
    for ingredient in ingredients_needed:
        ingredient_amount = ingredients_needed[ingredient]
        storage[ingredient] -= ingredient_amount
    money_gained = menu[beverage]["cost"]
    storage["money"] += money_gained


def make_beverage(
        beverage: str,
        ) -> None:
    """Prints a message when the beverage is ready.

    Parameters
    ----------
    beverage : str
        Lowercase string containing the name of the selected beverage."""
    print(f"Here is your {beverage} ☕. Enjoy!")


def coffee_machine():
    """Main program for running the coffee machine"""
    # Initialization parameters
    is_machine_running = True
    storage = {
        "water": INITIAL_WATER,
        "milk": INITIAL_MILK,
        "coffee": INITIAL_COFFEE,
        "money": INITIAL_MONEY,
    }

    while is_machine_running:
        command = input(f"What would you like? ({convert_menu_to_str(MENU)}): ").lower()
        if command == "off":
            # Turn off the machine
            return
        elif command == "report":
            print_report(storage)
        elif command in MENU.keys():

            are_resources_sufficient = check_resources(storage, MENU, command)
            if not are_resources_sufficient:
                continue

            total_amount = process_coins()
            is_transaction_valid = check_transaction(command, MENU, total_amount)
            if not is_transaction_valid:
                continue

            update_storage(command, MENU, storage)
            make_beverage(command)
        else:
            # Unavailable command
            print("Sorry, the beverage selected is not available, please try again")


if __name__ == "__main__":
    coffee_machine()
