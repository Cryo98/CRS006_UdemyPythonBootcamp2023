from resources import LOGO


def add(n1, n2):
    """Add two numbers and return the sum"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract the second number from the first and return the difference"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers and return the product"""
    return n1 * n2


def divide(n1, n2):
    """Divide the first number by the second and return the quotient"""
    return n1 / n2


OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    """Run the I/O operations for the calculator, allowing for multiple
    operations on the result."""
    print(LOGO)
    num1 = float(input("What's the first number?: "))
    isContinued = True
    while isContinued:
        for key in OPERATIONS:
            print(key)
        operation = input("Pick an operation symbol from the list above: ")
        num2 = float(input("What's the next number?: "))
        result = OPERATIONS[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        answer = input(f"Type 'y' to continue calculating with {result}, type 'n' to restart: ").lower()
        if answer == "y":
            num1 = result
        else:
            isContinued = False
            calculator()


if __name__ == "__main__":
    calculator()
