import random
from Day_012_NumberGuesserGame_resources import LOGO


def select_difficulty():
    """Asks the user for a difficulty level and returns the amount of attempts
    available"""
    difficulty = ""
    while difficulty != "hard" and difficulty != "easy":
        difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()
        if difficulty != "hard" and difficulty != "easy":
            print("Sorry, I didn't understand, please try again...")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    return attempts


def reduce_attempts(attempts):
    """Reduces the number of attempts and prints the current ones."""
    attempts -= 1
    print(f"You have {attempts} attempts remaining...")
    return attempts


def compare_numbers(a, b):
    """Compare numbers and prints relative position.
    It returns True if the numbers are equal, else False."""
    if a == b:
        return True
    elif a > b:
        print("Guess too high.")
    else:
        print("Guess too low.")
    return False


# Print intro
print(LOGO)
print("Welcome to the number guesser game!")
print("I'm thinking about a number between 1 and 100")
# Select a random number
selected_number = random.randint(1, 100)
# Select attempts based on difficulty
attempts = select_difficulty()
# Game loop until it is guessed or attempts are out
isGuessed = False
while not isGuessed and attempts > 0:
    guessed_number = int(input("Guess a number: "))
    isGuessed = compare_numbers(guessed_number, selected_number)
    # If it is not guessed reduce attempts available
    if not isGuessed:
        attempts = reduce_attempts(attempts)
# Result messages
if isGuessed:
    print("Congratulations! You guessed the number!")
else:
    print("Nice try, but you ran out of attempts.")
print(f"The number was {selected_number}.")
