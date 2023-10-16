import random


def main():
    print("Welcome to the PyPassword Generator!")
    print("How many letters would you like in your password?")
    nr_letters = int(input())
    print("How many symbols would you like?")
    nr_symbols = int(input())
    print("How many numbers would you like?")
    nr_numbers = int(input())
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print("Here is your password:", password)


def generate_password(
        nr_letters: int,
        nr_symbols: int,
        nr_numbers: int,
        ):
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ## FIRST METHOD
    # # Creates a list containing a number repeated a number of times based on
    # # the amount of letters, symbols or numbers desired for randomization.
    # # 0 for letters, 1 for symbols, 2 for numbers
    # characters_categories = list()
    # for _ in range(0, nr_letters):
    #     characters_categories.append(0)
    # for _ in range(0, nr_symbols):
    #     characters_categories.append(1)
    # for _ in range(0, nr_numbers):
    #     characters_categories.append(2)
    # # Runs a loop for the length of the desired password and extracts the
    # # choice from the list of characters categories, removing the character
    # # once selected as to ensure the exact amounts desired will be present.
    # password = ""
    # for _ in range(0, len(characters_categories)):
    #     character_category = random.choice(characters_categories)
    #     if character_category == 0:
    #         password += random.choice(LETTERS)
    #     elif character_category == 1:
    #         password += random.choice(SYMBOLS)
    #     else:
    #         password += random.choice(NUMBERS)
    #     characters_categories.remove(character_category)
    # return password
    ## SECOND METHOD
    password_list = []
    for _ in range(0, nr_letters):
        password_list.append(random.choice(LETTERS))
    for _ in range(0, nr_symbols):
        password_list.append(random.choice(SYMBOLS))
    for _ in range(0, nr_numbers):
        password_list.append(random.choice(NUMBERS))
    random.shuffle(password_list)
    return "".join(password_list)


if __name__ == '__main__':
    main()
